import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("RandomForest_best_model (2).joblib")

# List of expected columns (order must match model training)
expected_columns = [
    'vehicle_age', 'km_driven', 'mileage', 'engine', 'max_power', 'seats',
    'seller_type_Dealer', 'seller_type_Individual', 'seller_type_Trustmark Dealer',
    'fuel_type_CNG', 'fuel_type_Diesel', 'fuel_type_Electric', 'fuel_type_LPG', 'fuel_type_Petrol',
    'transmission_type_Automatic', 'transmission_type_Manual'
]

# App config
st.set_page_config(page_title="Car Price Estimator", layout="centered")

st.title("🚗 Car Price Estimator")
st.markdown("Predict the selling price of a used car based on its specifications.")

# Centered Input UI
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

    # Seller type
    'seller_type_Dealer': 1 if seller_type == 'Dealer' else 0,
    'seller_type_Individual': 1 if seller_type == 'Individual' else 0,
    'seller_type_Trustmark Dealer': 1 if seller_type == 'Trustmark Dealer' else 0,

    # Fuel type
    'fuel_type_CNG': 1 if fuel_type == 'CNG' else 0,
    'fuel_type_Diesel': 1 if fuel_type == 'Diesel' else 0,
    'fuel_type_Electric': 1 if fuel_type == 'Electric' else 0,
    'fuel_type_LPG': 1 if fuel_type == 'LPG' else 0,
    'fuel_type_Petrol': 1 if fuel_type == 'Petrol' else 0,

    # Transmission
    'transmission_type_Automatic': 1 if transmission_type == 'Automatic' else 0,
    'transmission_type_Manual': 1 if transmission_type == 'Manual' else 0
}

# Convert to DataFrame and reindex to match training
input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=expected_columns, fill_value=0)

# Centered predict button
st.markdown("---")
centered_button = st.columns([1, 1, 1])[1]

with centered_button:
    if st.button("🔍 Predict Selling Price"):
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Selling Price: ₹ {round(prediction):,}")
