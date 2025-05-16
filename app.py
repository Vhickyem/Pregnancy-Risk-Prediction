import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

# define the BPRatio Transformer
class BPRatio(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X["BPRatio"] = X["Systolic BP"] / X["Diastolic"]
        return X
    
# define the DropSomeFeatures Transformer
class DropSomeFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_drop=None):
        self.columns_to_drop = columns_to_drop

    def fit(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            self.columns_ = X.columns
        return self

    def transform(self, X):
        if isinstance(X, pd.DataFrame):
            return X.drop(columns=self.columns_to_drop, errors="ignore")
        else:
            raise TypeError("Input should be a Pandas DataFrame")

# Load the trained pipeline
model = joblib.load("pregnancy risk pipeline.pkl")

# Title and Subtitle
st.title("Maternal Risk Assessment Tool")
st.subheader("Predict whether a Pregnancy is High Risk or Low Risk")
st.markdown("Please, enter the patient's details in the following fields")

# Input form
with st.form("risk_form"):
    age = st.number_input("Age", min_value=10, max_value=65, value=None)
    systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=50, max_value=210, value=None)
    diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=50, max_value=130, value=None)
    bs = st.number_input("Blood Sugar Level (mmol/L)", min_value=3.0, max_value=20.0, value=None)
    body_temp = st.number_input("Body Temperature (F)", min_value=95, max_value=105, value=None)
    bmi = st.number_input("BMI", min_value=15.0, max_value=40.0, value=None)

    previous_complications = st.selectbox("Previous Complications", ["Yes", "No"], index=None)
    preexisting_diabetes = st.selectbox("Preexisting Diabetes", ["Yes", "No"], index=None)
    gestational_diabetes = st.selectbox("Gestational Diabetes", ["Yes", "No"], index=None)
    mental_health = st.selectbox("Mental Health Issues", ["Yes", "No"], index=None)

    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=160, value=None)

    #submit
    submit = st.form_submit_button("Assess Risk")

# Handle Prediction
if submit:
    # Convert inputs to match expected format
    input_dict = {
        "Age": age,
        "Systolic BP": systolic_bp,
        "Diastolic": diastolic_bp,
        "BS": bs,
        "Body Temp": body_temp,
        "BMI": bmi,
        "Previous Complications": 1 if previous_complications == "Yes" else 0,
        "Preexisting Diabetes": 1 if preexisting_diabetes == "Yes" else 0,
        "Gestational Diabetes": 1 if gestational_diabetes == "Yes" else 0,
        "Mental Health": 1 if mental_health == "Yes" else 0,
        "Heart Rate": heart_rate
    }

    input_df = pd.DataFrame([input_dict])

    # predict using the pipeline
    prediction = model.predict(input_df)[0]
    risk = "High Risk" if prediction == 0 else "Low Risk"

    # Display result
    st.success(f"This patient's pregnancy is at {risk}")