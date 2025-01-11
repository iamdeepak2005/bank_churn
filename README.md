# Bank Churn Prediction System

This repository contains the code for a **Bank Churn Prediction System** that uses machine learning to predict whether a customer will leave a bank (churn) or stay. The project integrates both frontend and backend components, utilizing React for the frontend and machine learning models (such as Gemini) for the reasoning tasks.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Setup](#project-setup)
- [Frontend Setup](#frontend-setup)
- [Backend Setup](#backend-setup)
- [Gemini Integration](#gemini-integration)
- [How to Run](#how-to-run)
- [Contributing](#contributing)

## Project Overview

The **Bank Churn Prediction System** is designed to predict customer churn using machine learning algorithms. The project is split into two parts:

1. **Frontend**: The user interface is built with **React**, which allows users to interact with the system and visualize the prediction results.
2. **Backend**: The backend is built with **Python** (Flask/FastAPI or similar) and handles data processing, model inference, and communication with the frontend.
3. **Gemini Integration**: For reasoning tasks, we use **Gemini**, a generative AI model, to provide explanations and insights for the prediction results.

## Technologies Used

- **Frontend**:
  - React
  - Axios (for API requests)
  - CSS (for styling)
  
- **Backend**:
  - Python
  - Flask/FastAPI (for API routes)
  - Scikit-learn (for churn prediction model)
  - Gemini (for reasoning tasks)
  
- **Machine Learning**:
  - Churn Prediction Model (trained on customer data)
  - Gemini (for generating insights and explanations)

## Project Setup

### Frontend Setup

To set up the frontend (React), follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/iamdeepak2005/bank_churn.git
Navigate to the frontend directory:

    ```bash
    cd frontend
Install the required dependencies:

    ```bash
    npm install
Start the React development server:

    ```bash
    npm start
This will start the frontend server and open the app in your browser (usually at http://localhost:3000).

Backend Setup
To set up the backend (Python with Flask/FastAPI), follow these steps:

Navigate to the backend directory:

    ```bash
    cd backend
Create and activate a virtual environment (if not already done):

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
Start the backend server:

    ```bash
    python app.py  # Or use any script for starting your server, depending on the framework (Flask/FastAPI)
This will start the backend server (usually at http://localhost:5000).

# Gemini Integration
Gemini will be used for providing reasoning and insights into the churn prediction. Here's how Gemini is integrated into the project:

**Gemini Model**: The Gemini model will be used for generating explanations and predictions for the churn model. This allows users to understand the rationale behind the predictions made by the churn model.

**API Call**: The backend communicates with Gemini via API requests. The predictions from the machine learning model will be sent to Gemini, which will generate a reasoning explanation and return it to the frontend.

Example API call:

python
    ```bash
    import requests
    def get_gemini_reasoning(prediction_data):
        response = requests.post('http://gemini-api-url', json=prediction_data)
        reasoning = response.json()
        return reasoning

Usage: When the frontend makes a request to the backend for a churn prediction, the backend not only returns the prediction but also sends the input data to Gemini for a detailed explanation.

How to Run
Frontend:

Navigate to the frontend directory.
Install the necessary dependencies with npm install.
Run the React app with npm start.
Backend:

Navigate to the backend directory.
Install the necessary dependencies with pip install -r requirements.txt.
Start the backend server using python app.py.
Gemini: Ensure the Gemini model is set up and accessible through an API endpoint to generate reasoning for predictions.

Once both servers (frontend and backend) are running, your application should be accessible in the browser.

**Contributing**
We welcome contributions to this project! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit them (git commit -am 'Add new feature').
Push to your branch (git push origin feature-name).
Open a pull request.
Additional Markdown Features Used
Headings: # for main headings, ## for subheadings.
Bold Text: **text** for highlighting key terms like React, Gemini.
Code Blocks: For code snippets, use three backticks (```) before and after the code.
Lists: Used for enumerating instructions and technologies.
