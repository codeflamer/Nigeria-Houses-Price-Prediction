# Nigeria Housing Price Prediction - Backend Service

This is the backend service for the Nigeria Housing Price Prediction application. It provides a RESTful API for house price predictions using FastAPI.

## Project Structure

```
backend/
├── main.py           # FastAPI application entry point
├── util.py           # Utility functions for prediction
├── requirements.txt  # Python dependencies
├── Dockerfile       # Container configuration
├── .dockerignore    # Docker ignore rules
├── request.json     # Example request payload
└── artifacts/       # Model artifacts directory
```

## API Endpoints

### 1. Health Check

- **Endpoint**: `GET /`
- **Description**: Basic health check endpoint
- **Response**: `{"message": "Hello World"}`

### 2. Price Prediction

- **Endpoint**: `POST /predict`
- **Description**: Predict house price based on property features
- **Request Body**:
  ```json
  {
    "bedrooms": int,
    "bathrooms": int,
    "toilets": int,
    "parking_space": int,
    "title": string,
    "town": string,
    "state": string
  }
  ```
- **Response**: `{"price": float}`

## Setup

### Local Development

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python main.py
   ```
   The server will start at `http://localhost:8000`

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t nigeria-housing-backend .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 nigeria-housing-backend
   ```

## API Documentation

Once the server is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Dependencies

- Python 3.9+
- FastAPI 0.95.2
- Uvicorn 0.22.0
- NumPy 1.24.3
- Pandas 2.0.3
- Scikit-learn 1.3.0
- Other dependencies listed in requirements.txt

## Development

The backend uses FastAPI for high performance and automatic API documentation. The prediction logic is implemented in `util.py`, which loads the trained model and handles the prediction process.

## Testing

You can test the API using the example request in `request.json`:

```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d @request.json
```
