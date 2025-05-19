import streamlit as st
import numpy as np
import joblib
from PIL import Image

# Load model
model = joblib.load('./model/heart_model.pkl')

# --- Top-Right Heart Icon ---
col1, col2, col3 = st.columns([10, 1, 1])
with col1:
    heart_icon = Image.open("./assets/heart.jpg")
    st.image(heart_icon, width=80)

# --- Page Navigation ---
page = st.sidebar.radio("Navigation", ["Heart Attack Predictor", "About"])

# --- Prediction Page ---
if page == "Heart Attack Predictor":
    st.title("💓 Heart Attack Risk Predictor")

    # --- User Inputs ---
    age = st.slider("Age", 20, 100)
    gender = st.selectbox("Gender", ["Male", "Female"])
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40.0, format="%.3f", step=0.001)
    sys_bp = st.number_input("Systolic BP", min_value=70.0, format="%.3f", step=0.001)
    dia_bp = st.number_input("Diastolic BP", min_value=40.0, format="%.3f", step=0.001)
    sugar = st.number_input("Blood Sugar (mg/dL)", format="%.3f", step=0.001)
    ckmb = st.number_input("CK-MB", format="%.3f", step=0.001)
    troponin = st.number_input("Troponin", format="%.3f", step=0.001)

    # --- Prediction ---
    if st.button("Predict"):
        gender_bin = 1 if gender == "Male" else 0
        features = np.array([[age, gender_bin, heart_rate, sys_bp, dia_bp, sugar, ckmb, troponin]])

        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0]  # probabilities for classes [0, 1]

        risk_level = proba[1]  # probability of class '1' = "At Risk"
        risk_percent = risk_level * 100

        if prediction == 1:
            st.subheader(f"⚠️ At Risk of Heart Attack! (Risk Level: {risk_percent:.2f}%)")
        else:
            st.subheader(f"✅ No Immediate Risk (Risk Level: {risk_percent:.2f}%)")


# --- About Page ---
elif page == "About":
    st.title("ℹ️ About This App")
    st.markdown("""
        This application predicts the risk of a **heart attack** based on medical input features like:

        - Age, Gender
        - Heart rate, Blood pressure
        - Blood sugar, CK-MB, and Troponin levels

        The model is trained on a dataset from **Kaggle**, and uses **machine learning** to determine risk.

        ---
        - **Developed by:** Hasan Uddin (abcnizamd@gmail.com)
        - **Model:** Trained with Scikit-learn  
        - **Interface:** Built with Streamlit
    """)
    col1, col2, col3 = st.columns([10, 1, 1])
    with col3:
        heart_icon = Image.open("./assets/icon.png")
        st.image(heart_icon, width=80)
