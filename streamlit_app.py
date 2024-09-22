import streamlit as st

st.title("❤️ Heart health classifier app")
st.write(
    "This is an app for getting a prediction for heart disease. Please input your data and a prediction will be produced"
)

age = st.slider("How old are you?", 0, 100, 40)
sex = st.radio(
    "Are you male or female",
    ["Male", "Female"],
)
chest_pain = st.radio(
    "What type of chest pain do you have?",
    ["Asymptomatic",
      "Non-anginal pain",
      "Atypical angina",
      "Typical angina" ],
)

resting_bp = st.slider("Resting blood pressure?", 90, 200, 150, 5)

cholesterol = st.slider("Cholesterol (mg.dL)?", 100, 600, 200, 10)

blood_sugar = st.toggle("Fasting blood sugar > 120 mg/dL?")

ecg = st.radio(
    "ECG results?",
    ["Normal",
      "Abnormality",
      "Hypertrophy"],
)

heart_rate = st.slider("Heart rate during Thallium test?", 70, 200, 120, 5)

exercise_pain = st.toggle("Pain during exercise?")

old_peak = st.slider("Old peak?", 0., 7., 2., 0.5)

slope = st.radio(
    "Slope?",
    ["Ascending",
      "Flat",
      "Descending"],
)

vessels = st.slider("Number of major vessels colored by flourosopt?", 1, 3, 1)

thal = st.radio(
    "Thalassemia?",
    ["Normal",
      "Defect",
      "Reversible"],
)

st.button("Make prediction", type="primary")

from predict import Predictor
import pandas as pd
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
test_row = [37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2]
test_data = pd.DataFrame(data=[test_row], columns=col_heads)
prediction = predictor(test_data)
st.header(str(prediction))