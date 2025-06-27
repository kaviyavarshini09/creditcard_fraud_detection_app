import streamlit as st
import numpy as np
import pickle
import os

# === Load the Model ===
model_path = os.path.join("model", "xgb_model.pkl")

try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error(f"❌ Model file not found at: {model_path}")
    st.stop()

# === Streamlit UI ===
st.set_page_config(page_title="Fraud Detection App")
st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter the 30 features below to check if the transaction is **Fraudulent** or **Legitimate**.")

# === Input Fields ===
input_values = []
for i in range(30):
    val = st.text_input(f"Feature {i+1}", value="0.0")
    try:
        input_values.append(float(val))
    except ValueError:
        st.warning(f"⚠️ Feature {i+1} must be a valid number.")

# === Predict Button ===
if st.button("🔍 Predict Fraud"):
    if len(input_values) == 30:
        input_array = np.array([input_values])
        prediction = model.predict(input_array)[0]

        if prediction == 1:
            st.error("❌ Fraudulent Transaction Detected!")
        else:
            st.success("✅ Legitimate Transaction")
    else:
        st.warning("Please fill in all 30 features with valid numeric values.")
