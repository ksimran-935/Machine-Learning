import streamlit as st
import pandas as pd
import joblib
import os
import urllib.request

# ========== Step 1: Download model from Google Drive if not present ==========
MODEL_URL = "https://drive.google.com/uc?export=download&id=1ziYd-KdiGqeyCl38LK7m19MaiEoemSIX"
MODEL_PATH = "RandomForest_best_model.joblib"

if not os.path.exists(MODEL_PATH):
    with st.spinner("📥 Downloading model..."):
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

# ========== Step 2: Load model ==========
model = joblib.load(MODEL_PATH)

# ========== Step 3: Expected features ==========
expected_columns = [
    'vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats',
    'seller_type_Dealer', 'seller_type_Individual', 'seller_type_Trustmark Dealer',
    'fuel_type_CNG', 'fuel_type_Diesel', 'fuel_type_Electric', 'fuel_type_LPG', 'fuel_type_Petrol',
    'transmission_type_Automatic', 'transmission_type_Manual'
]

# ========== Step 4: Streamlit UI ==========
st.set_page_config(page_title="Car Price Estimator", layout="centered")
st.title("🚗 Car Price Estimator")
st.markdown("Predict the selling price of a used car based on its specifications.")

# Centered input fields
with st.container():
    st.markdown("### ✍️ Enter Car Details")

    col1, col2 = st.columns(2)

    with col1:
        vehicle_age = st.number_input("Vehicle Age (Years)", min_value=0, max_value=30, value=5)
        km_driven = st.number_input("Kilometers Driven", min_value=1000, max_value=500000, step=1000, value=30000)
        mileage = st.number_input("Mileage (kmpl)", min_value=5.0, max_value=40.0, step=0.1, value=20.0)
        engine = st.number_input("Engine Capacity (CC)", min_value=600, max_value=5000, step=100, value=1200)

    with col2:
        max_power = st.number_input("Max Power (BHP)", min_value=20.0, max_value=400.0, step=5.0, value=85.0)
        seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8, 9, 10])
        seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual', 'Trustmark Dealer'])
        fuel_type = st.selectbox("Fuel Type", ['CNG', 'Diesel', 'Electric', 'LPG', 'Petrol'])
        transmission_type = st.selectbox("Transmission Type", ['Automatic', 'Manual'])

# One-hot encoding manually
input_data = {
    'vehicle_age': vehicle_age,
    'km_driven': km_driven,
    'mileage': mileage,
    'engine': engine,
    'max_power': max_power,
    'seats': seats,

    'seller_type_Dealer': int(seller_type == 'Dealer'),
    'seller_type_Individual': int(seller_type == 'Individual'),
    'seller_type_Trustmark Dealer': int(seller_type == 'Trustmark Dealer'),

    'fuel_type_CNG': int(fuel_type == 'CNG'),
    'fuel_type_Diesel': int(fuel_type == 'Diesel'),
    'fuel_type_Electric': int(fuel_type == 'Electric'),
    'fuel_type_LPG': int(fuel_type == 'LPG'),
    'fuel_type_Petrol': int(fuel_type == 'Petrol'),

    'transmission_type_Automatic': int(transmission_type == 'Automatic'),
    'transmission_type_Manual': int(transmission_type == 'Manual')
}

input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=expected_columns, fill_value=0)

# Centered predict button
st.markdown("---")
centered_button = st.columns([1, 1, 1])[1]

with centered_button:
    if st.button("🔍 Predict Selling Price"):
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Selling Price: ₹ {round(prediction):,}")
