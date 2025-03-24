import pickle
import numpy as np


__model = None
__category_to_index = None
__state_town_relationships = None



def get_price_prediction(bedrooms, bathrooms, toilets, parking_space, title, town, state):

    title_index = __category_to_index["title"][title]
    town_index = __category_to_index["town"][town]
    state_index = __category_to_index["state"][state]

    features = np.array([bedrooms, bathrooms, toilets, parking_space, 
                           title_index, town_index, state_index]).reshape(1, -1)

    prediction = __model.predict(features)[0]
    predicted_price = np.expm1(prediction)

    return f'Predicted Price: ₦{predicted_price:.2f}'



def load_artifacts():
    global __model, __category_to_index, __state_town_relationships
    try:
        with open("./artifacts/model.pickle", "rb") as f:
            __model = pickle.load(f)
        with open("./artifacts/category_indexs.pickle", "rb") as f:
            __category_to_index = pickle.load(f)
    except FileNotFoundError as e:
        print(f"Error: Could not find one of the required files: {e}")
    except Exception as e:
        print(f"Error loading models: {e}")

if __name__ == "__main__":
    load_artifacts()
    # print(__category_to_index)
    # print(get_price_prediction(3, 2, 1, 1, "Semi Detached Bungalow", "Ikeja", "Lagos"))
