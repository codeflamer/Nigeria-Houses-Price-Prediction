# Nigeria Housing Price Prediction Project

A comprehensive machine learning application for predicting house prices in Nigeria. This project consists of both a frontend web interface and a backend API service.

## Project Overview

This application helps users predict house prices in Nigeria based on various property features such as location, number of rooms, and property type. The project is built with a modern architecture separating frontend and backend concerns.

## Project Structure

```
Nigeria Housing/
├── App/                    # Frontend Application
│   ├── app.py             # Gradio web interface
│   ├── model/             # Model artifacts
│   ├── images/            # State visualizations
│   └── requirements.txt   # Frontend dependencies
│
├── backend/               # Backend API Service
│   ├── main.py           # FastAPI application
│   ├── util.py           # Prediction utilities
│   ├── artifacts/        # Model artifacts
│   └── requirements.txt  # Backend dependencies
│
└── README.md             # This file
```

## Components

### 1. Frontend (App/)

- Built with Gradio for a user-friendly interface
- Features:
  - Interactive form for property details
  - Dynamic state and town selection
  - Visual representation of state data
  - Real-time price predictions
  - Responsive design

### 2. Backend (backend/)

- RESTful API built with FastAPI
- Features:
  - Price prediction endpoint
  - Health check endpoint
  - API documentation (Swagger/ReDoc)
  - Docker support
  - Model serving

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

### Running the Application

#### Option 1: Run Frontend Only

1. Navigate to the App directory
2. Follow setup instructions in `App/README.md`

#### Option 2: Run Backend Only

1. Navigate to the backend directory
2. Follow setup instructions in `backend/README.md`

#### Option 3: Run Both Services

1. Start the backend service first
2. Start the frontend service
3. Access the application through the frontend URL

## Features

- **Price Prediction**: Accurate house price estimates based on:

  - Location (State and Town)
  - Property Features (bedrooms, bathrooms, toilets)
  - Property Type
  - Additional Amenities (parking spaces)

- **Interactive Interface**:

  - Dynamic form updates
  - Real-time predictions
  - Visual data representation
  - User-friendly input validation

- **API Integration**:
  - RESTful endpoints
  - JSON request/response format
  - Comprehensive API documentation
  - Docker containerization support

## Technology Stack

- **Frontend**:

  - Gradio
  - Python
  - NumPy
  - Pandas
  - Matplotlib
  - Seaborn

- **Backend**:
  - FastAPI
  - Uvicorn
  - Scikit-learn
  - Docker

## Contributing

Feel free to submit issues and enhancement requests!
