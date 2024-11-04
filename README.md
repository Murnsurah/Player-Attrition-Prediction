# Player-Attrition-Prediction
This repository contains a churn detection system using supervised learning techniques to identify players likely to churn. The project establishes a baseline model addressing player attrition challenges in the gaming industry, offering insights into user behavior and helping improve retention strategies.

## Table of Contents

- [Technologies Used]
- [Usage]
- [Features]
- [License]
- [Contact]



## Technologies Used

This project is built using the following tools and libraries:

- **Python**: Programming language used for development
- **FastAPI**: Framework for building the API
- **Scikit-Learn**: Machine learning library for model training
- **Pandas**: Data manipulation library
- **NumPy**: Library for numerical operations
- **Joblib**: Library for model serialization



## Usage

1. Run the FastAPI server:
uvicorn main:app --reload

Then open your browser and go to  http://127.0.0.1:8000.

2. Send a POST request to the /predict endpoint with transaction data in the following format:
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
	"year": 2020
}
3. Receive a response with churn prediction and probability:
{
    {
  "churn_prediction": true,
  "churn_probability": 0.65
}
}

## Features
- Simple and effective fraud detection using supervised learning techniques.
- RESTful API built with FastAPI for easy integration.
- Detailed logging of predictions and transactions.
- Well-structured codebase that allows for easy modifications and enhancements.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
For any inquiries or feedback, please contact me at https://murnsurah.github.io/Monsurat-Afolabi.github.io/
