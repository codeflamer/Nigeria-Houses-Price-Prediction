# Nigeria Housing Price Prediction

A machine learning application that predicts house prices in Nigeria using various features.

## Project Structure

```
App/
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── model/             # Model artifacts
├── images/            # State visualizations
├── .gradio/          # Gradio config
└── flagged/          # Flagged predictions
```

## Setup

1. Navigate to App directory
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

```bash
python app.py
```

Then open http://127.0.0.1:7860 in your browser.

## Features

- Price prediction based on:
  - Bedrooms, bathrooms, toilets
  - Parking spaces
  - Property title
  - State and town location
- Interactive state selection
- State data visualization
- Price in Nigerian Naira (₦)

## Requirements

- Python 3.9+
- See requirements.txt for package versions

## Troubleshooting

1. Verify all model files exist
2. Check dependencies are installed
3. Ensure Python 3.9+ is used
4. Run from App directory
