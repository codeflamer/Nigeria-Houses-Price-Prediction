import pandas as pd
import numpy as np
import pickle
import gradio as gr
import json
from PIL import Image

# Initialize variables
category_label = None
lr = None
scaler = None
state_town_map = None
path_to_image = None

try:
    # Load category labels
    with open("./model/category_indexs.pickle", "rb") as f:
        category_label = pickle.load(f)
    
    # Load model
    with open("./model/model.pickle", "rb") as f:
        lr = pickle.load(f)
    
    # Load scaler
    with open("./model/scaler.pickle", "rb") as f:
        scaler = pickle.load(f)
    
    with open("./model/state_town_relationship.json", "r") as f:
        state_town_map = json.load(f)
    
    with open("./model/image_to_path.json", "r") as f:
        path_to_image = json.load(f)
    
    print("All artifacts loaded successfully!")

except FileNotFoundError as e:
    print(f"Error: Could not find one of the required files: {e}")
except Exception as e:
    print(f"Error loading models: {e}")

def update_towns(state):
    if state in state_town_map:
        image_path = path_to_image[state]
        image = Image.open(image_path)
        return gr.Dropdown(choices=state_town_map[state]), image
    return gr.Dropdown(choices=[]), None

def calculate_price(bedrooms, bathrooms, toilets, parking_space, title, town, state):
    try:
        # Check if all models are loaded
        if None in [category_label, lr, scaler]:
            return "Error: Models not properly loaded. Please check the console for details."
        
        # Get category indices
        title_index = category_label["title"][title]
        town_index = category_label["town"][town]
        state_index = category_label["state"][state]
        
        # Create and transform features
        features = np.array([bedrooms, bathrooms, toilets, parking_space, 
                           title_index, town_index, state_index]).reshape(1, -1)
        feature_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = lr.predict(feature_scaled)[0]
        predicted_price = np.expm1(prediction)
        
        return f'Predicted Price: ₦{predicted_price:,.2f}'
    
    except KeyError as e:
        return f"Error: Invalid input category. Please check title, town, or state values. Details: {e}"
    except Exception as e:
        return f"Error during prediction: {e}"

# Create the interface
with gr.Blocks() as iface:
    gr.Markdown("# Nigerian House Price Prediction")
    gr.Markdown("This app predicts the price of a house in Nigeria based on its features.")
    
    with gr.Row():
        with gr.Column():
            bedrooms = gr.Number(label="Number of Bedrooms", value=1)
            bathrooms = gr.Number(label="Number of Bathrooms", value=1)
            toilets = gr.Number(label="Number of Toilets", value=1)
            parking_space = gr.Number(label="Number of Parking Spaces", value=0)
            title = gr.Dropdown(
                choices=list(category_label["title"].keys()) if category_label else [], 
                label="Property Title"
            )
            state = gr.Dropdown(
                choices=list(state_town_map.keys()) if state_town_map else [],
                label="State"
            )
            town = gr.Dropdown(choices=[], label="Town")
            
            predict_btn = gr.Button("Predict Price", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(label="Prediction")
            image = gr.Image(label="State pie chart",type="pil")
    
    # Update town choices when state changes
    state.change(fn=update_towns, inputs=state, outputs=[town,image])
    
    # Predict price when button is clicked
    predict_btn.click(
        fn=calculate_price,
        inputs=[bedrooms, bathrooms, toilets, parking_space, title, town, state],
        outputs=output
    )

if __name__ == "__main__":
    iface.launch()
