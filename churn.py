import os
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn  # Make sure to import uvicorn at the top

# Get the absolute path to the model directory
model_dir = os.path.join(os.path.dirname(__file__),  'churn_model.pkl')

# Check if the model file exists
if not os.path.exists(model_dir):
    raise FileNotFoundError(f"Model file not found at {model_dir}")



# Load the trained model
model = joblib.load(model_dir)

print(f"Current working directory: {os.getcwd()}")
print(f"Looking for model at: {model}")

# Initialise FastAPI instance with metadata
app = FastAPI(
    title="Player Attrition API",
    version="0.1.0",
    description=( 
        "**This API offers endpoints for detecting potential player attrition using a machine learning model developed through supervised learning techniques. By analyzing a comprehensive set of gaming features, the model predicts the likelihood of a user churning, or discontinuing play. The primary goal of this API is to assist the gaming industry in identifying players at risk of attrition, thereby enabling proactive measures to retain them. "
        "By integrating this API into their systems, it provides accurate predictions and aims to help gaming companies mitigate potential losses and enhance player engagement.**"
    ),
    contact={
        "name": "Monsurat Afolabi",
        "url": "https://murnsurah.github.io/Monsurat-Afolabi.github.io/"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    },
)

# Define the data schema for input features
class PlayerAttrition(BaseModel):
    level_id: int
    attempt_result: int
    attempt_duration: float
    f_reststep: float
    extra_help_used: int
    avg_attempt_duration: float
    avg_clearance_rate: float
    avg_clearance_duration: float
    avg_num_retries: float
    year: int

# Root Endpoint
@app.get("/", summary="Root Endpoint")
def root():
    """Welcome message and API overview."""
    return {
        "message": "Welcome to the Player Attrition API",
        "details": "Visit '/docs' for a comprehensive overview of available endpoints and to test the API."
    }

# Root Details
@app.get("/api/v0.1.0/root/", tags=["Root"], summary="Root Details")
def read_root_details():
    """Detailed root information, including API overview and key endpoints."""
    return {
        "overview": "This API provides endpoints for predicting player attrition in gaming applications using machine learning models.",
        "endpoints": [
            {
                "path": "/",
                "description": "Root endpoint offering a welcome message and a high-level overview of the API functionality."
            },
            {
                "path": "/api/v0.1.0/predict",
                "description": "Predicts the likelihood of a player churning based on game interaction features, providing insights to help enhance player retention strategies."
            },
        ]
    }

# Create a router for player attrition prediction
player_attrition_router = APIRouter()

@player_attrition_router.post("/predict", summary="Predict Player Attrition", tags=["Player Attrition Prediction"])
def predict(player_data: PlayerAttrition): 
    """
    Predicts whether a player is likely to churn based on their game interaction data.
    
    - **player_data**: Player data, including features such as level_id, attempt_result, attempt_duration,
      extra_help_used, avg_attempt_duration, avg_clearance_rate, avg_clearance_duration,
      avg_num_retries, and the year.
    
    - Returns:
        - **churn_prediction** (bool): True if churn is predicted, False otherwise.
        - **churn_probability** (float): Probability of churn (between 0 and 1).
    """
    # Prepare the input data for model prediction
    data = np.array([[ 
        player_data.level_id, 
        player_data.attempt_result, 
        player_data.attempt_duration, 
        player_data.f_reststep, 
        player_data.extra_help_used,
        player_data.avg_attempt_duration,
        player_data.avg_clearance_rate,
        player_data.avg_clearance_duration,
        player_data.avg_num_retries,
        player_data.year
    ]])

    # Make a prediction using the trained model
    prediction = model.predict(data)
    churn_probability = model.predict_proba(data)[0][1]  # Probability of churn

    # Return the prediction result
    return {
        "churn_prediction": bool(prediction[0]),  # True for churn, False otherwise
        "churn_probability": churn_probability  # Probability of churn (between 0 and 1)
    }

# Include the churn detection router
app.include_router(player_attrition_router, prefix="/api/v0.1.0", tags=["Player Attrition Prediction"])

# Run the API with uvicorn
if __name__ == '__main__':
    import uvicorn  # Import here to avoid NameError in other environments
    uvicorn.run(app, host='127.0.0.1', port=8000)