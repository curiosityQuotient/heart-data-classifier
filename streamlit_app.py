import streamlit as st
from predict import Predictor
import pandas as pd

st.title("❤️ Heart health classifier app")
st.write(
    "This is an app for getting a prediction for heart disease. Please input your data and a prediction will be produced"
)

age = st.slider("How old are you?", 0, 100, 40)
sex = st.radio(
    "Are you male or female",
    ["Male", "Female"],
)
# parse sex variable
sex_val = 1
if sex == "Female":
    sex_val = 0

chest_pain = st.radio(
    "What type of chest pain do you have?",
    ["Asymptomatic",
      "Non-anginal pain",
      "Atypical angina",
      "Typical angina" ],
)
chest_pain_val = 0
if chest_pain == "Non-anginal pain":
    chest_pain_val = 1
elif chest_pain == "Atypical angina":
    chest_pain_val = 2
elif chest_pain == "Typical angina":
    chest_pain_val = 3

resting_bp = st.slider("Resting blood pressure?", 90, 200, 150, 5)

cholesterol = st.slider("Cholesterol (mg.dL)?", 100, 600, 200, 10)

blood_sugar = st.toggle("Fasting blood sugar > 120 mg/dL?")
bs_val = 0
if blood_sugar:
    bs_val = 1

ecg = st.radio(
    "ECG results?",
    ["Normal",
      "Abnormality",
      "Hypertrophy"],
)
ecg_val = 0
if ecg == "Abnormality":
    ecg_val = 1
elif ecg == "Hypertrophy":
    ecg_val = 2

heart_rate = st.slider("Heart rate during Thallium test?", 70, 200, 120, 5)

exercise_pain = st.toggle("Pain during exercise?")
pain_val = 0
if exercise_pain:
    pain_val = 1

old_peak = st.slider("Old peak?", 0., 7., 2., 0.5)

slope = st.radio(
    "Slope?",
    ["Ascending",
      "Flat",
      "Descending"],
)
slope_val = 0
if slope == "Flat":
    slope_val = 1
elif slope == "Descending":
    slope_val = 2

vessels = st.slider("Number of major vessels colored by flourosopt?", 1, 3, 1)

thal = st.radio(
    "Thalassemia?",
    ["Normal",
      "Defect",
      "Reversible"],
)
thal_val = 0
if thal == "Defect":
    thal_val = 1
elif thal == "Reversible":
    thal_val = 2

predictor = Predictor("./mlruns/493198603292191274/90a28e8d530d4a93abb89ec2eae9cdcb/artifacts/model/model.pkl")
col_heads = [
        "age",
        "sex",
        "chest pain type",
        "resting blood pressure",
        "chol",
        "fasting blood sugar",
        "resting ECG",
        "max heart rate",
        "exang",
        "oldpeak",
        "slope",
        "number vessels flourosopy",
        "thal",
    ]
#test_row = [37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2]
user_inputs = [
        age,
        sex_val,
        chest_pain_val,
        resting_bp,
        cholesterol,
        bs_val,
        ecg_val,
        heart_rate,
        pain_val,
        old_peak,
        slope_val,
        vessels,
        thal_val
    ]

test_data = pd.DataFrame(data=[user_inputs], columns=col_heads)

st.header("Model prediction")

if st.button("Make prediction"):
    predictor.predict(test_data)
    prediction = predictor.predictions[0]
    if prediction == 1:
        st.subheader("The model predicts you have heart disease.")
    else:
        st.subheader("The model predicts you do not have heart disease.")
else:
    st.subheader("Awaiting data")