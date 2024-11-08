# Player-Attrition-Prediction
This repository contains a churn detection system using supervised learning techniques to identify players likely to churn. The project establishes a baseline model addressing player attrition challenges in the gaming industry, offering insights into user behavior and helping improve retention strategies.

## Table of Contents
- Dataset Used
- Technologies Used
- Usage
- Features
- Contact

## Dataset

The dataset used for this project is stored in a Google Drive folder. You can access it using the link below:

Dataset : https://drive.google.com/file/d/1oN5xznt9-xMgRTKzKVcob-jbIQ2XEgyd/view?usp=sharing




## Technologies Used

This project is built using the following tools and libraries:

- **Python**: Programming language used for development
- **FastAPI**: Framework for building the API
- **Scikit-Learn**: Machine learning library for model training
- **Pandas**: Data manipulation library
- **NumPy**: Library for numerical operations
- **Joblib**: Library for model serialization


## Usage

1. **Run the FastAPI server**: Start the API server by running:
   ```bash
   uvicorn main:app --reload
2. **Send a POST request**: Send a POST request to the `/predict` endpoint with player data in JSON format. Here’s an example request:

   ```json
   {
       "level_id": 1,
       "attempt_result": 10,
       "attempt_duration": 20.5,
       "f_reststep": 0.5,
       "extra_help_used": 6,
       "avg_attempt_duration": 10.5,
       "avg_clearance_rate": 12.5,
       "avg_clearance_duration": 20.5,
       "avg_num_retries": 8.6,
       "year": 2020
   }

3. **Receive the response**: The API will return a response with the churn prediction and probability:

   ```json
   {
       "churn_prediction": true,
       "churn_probability": 0.65
   }


## Features
- Player Churn Prediction: Uses supervised learning to predict if a player is likely to churn, helping the gaming industry identify at-risk players.
- RESTful API with FastAPI: Provides a straightforward endpoint for predictions, making it easy to integrate with other applications.
- Detailed Logging: Logs predictions and transactions for better monitoring and analysis.
- Modular Codebase: Well-structured code that allows for easy modifications and enhancements.


## Contact
For any inquiries or feedback, please contact me at https://murnsurah.github.io/Monsurat-Afolabi.github.io/
