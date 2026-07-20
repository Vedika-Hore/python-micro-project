import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️")

st.title("❤️ Heart Disease Prediction")
st.write("Enter the patient's details below.")

# Input Fields
age = st.number_input("Age", min_value=1, max_value=120, value=40)
sex = st.selectbox("Sex", ["M", "F"])
chestPainType = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
restingBP = st.number_input("Resting Blood Pressure", value=120)
cholesterol = st.number_input("Cholesterol", value=200)
fastingBS = st.selectbox("Fasting Blood Sugar", [0, 1])
restingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
maxHR = st.number_input("Maximum Heart Rate", value=150)
exerciseAngina = st.selectbox("Exercise Angina", ["N", "Y"])
oldpeak = st.number_input("Oldpeak", value=1.0, step=0.1)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Predict Button
if st.button("Predict"):

    # Create DataFrame
    sample = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "ChestPainType": [chestPainType],
        "RestingBP": [restingBP],
        "Cholesterol": [cholesterol],
        "FastingBS": [fastingBS],
        "RestingECG": [restingECG],
        "MaxHR": [maxHR],
        "ExerciseAngina": [exerciseAngina],
        "Oldpeak": [oldpeak],
        "ST_Slope": [st_slope]
    })

    # One-Hot Encoding
    sample = pd.get_dummies(sample)

    # Match training columns
    sample = sample.reindex(columns=columns, fill_value=0)

    # Scale input (if scaler exists)
    if scaler is not None:
        sample = scaler.transform(sample)

    # Prediction
    prediction = model.predict(sample)

    # Display Result
    if prediction[0] == 1:
        st.error("❤️ Heart Disease: Yes")
    else:
        st.success("💚 Heart Disease: No")