# Flood Prediction Linear Regression

# Overview

This project predicts FloodProbability using LinearRegression on the Flood Prediction Dataset from Kaggle.

# Dataset

File: data/flood.csv
Rows: 50000
Columns: 21
Features: 20 numerical variables
Target: FloodProbability
Features
MonsoonIntensity
TopographyDrainage
RiverManagement
Deforestation
Urbanization
ClimateChange
DamsQuality
Siltation
AgriculturalPractices
Encroachments
IneffectiveDisasterPreparedness
DrainageSystems
CoastalVulnerability
Landslides
Watersheds
DeterioratingInfrastructure
PopulationScore
WetlandLoss
InadequatePlanning
PoliticalFactors

# Project Structure

Flood_Prediction_LinearRegression/
├── .venv/
├── data/
│ └── flood.csv
├── models/
│ ├── linear_regression_model.pkl
│ └── scaler.pkl
├── notebooks/
│ └── flood.ipynb
├── streamlit_app/
│ ├── app.py
│ ├── utils.py
│ ├── api_groq.txt
│ └── requirements_streamlit.txt
├── requirements.txt
└── README.md

# Setup

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Model Training

Train the model in notebooks/flood.ipynb.
The pipeline includes:
Data loading
EDA
Duplicate removal
Train/test split
Standardization
Linear Regression training
Evaluation with MAE, MSE, R2, Cross Validation
Saving model with joblib

# Run Streamlit App

pip install -r streamlit_app/requirements_streamlit.txt
streamlit run streamlit_app/app.py

# Streamlit Features

Manual input for 20 features
FloodProbability prediction
Input summary table
Simple visualization
Groq AI explanation in Vietnamese

# Model Artifacts

models/linear_regression_model.pkl
models/scaler.pkl

# Author

To Anh Phap
