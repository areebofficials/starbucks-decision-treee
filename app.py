import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="Starbucks Calorie Predictor",
    page_icon="☕"
)

@st.cache_resource
def load_model():
    model_path = "starbucks_decision_tree.pkl"
    # Check kar rahe hain ke file repository mein majood hai ya nahi
    if not os.path.exists(model_path):
        return None
    with open(model_path, "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("☕ Starbucks Calorie Predictor")
st.write("Enter nutritional values to predict the calorie category.")

# Agar model successfully load nahi hua to screen par warning dikhaye ga
if model is None:
    st.error("⚠️ Error: 'starbucks_decision_tree.pkl' file aapki GitHub repository mein nahi mili! Pehle file upload karein.")
else:
    sugar = st.number_input("Sugar (g)", min_value=0.0, value=30.0)
    caffeine = st.number_input("Caffeine (mg)", min_value=0.0, value=150.0)
    fat = st.number_input("Fat (g)", min_value=0.0, value=8.0)
    protein = st.number_input("Protein (g)", min_value=0.0, value=5.0)
    price = st.number_input("Price (USD)", min_value=0.0, value=5.0)

    if st.button("Predict"):
        inputs = pd.DataFrame([{
            "Sugar_g": sugar,
            "Caffeine_mg": caffeine,
            "Fat_g": fat,
            "Protein_g": protein,
            "Price_USD": price
        }])

        prediction = model.predict(inputs)[0]
        st.success(f"Predicted category: {prediction}")

st.caption("Educational project using a small sample dataset.")
