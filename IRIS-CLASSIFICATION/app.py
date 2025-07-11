import streamlit as st
import numpy as np
import joblib
import os

# Get the full path of the model regardless of current directory
model_path = os.path.join(os.path.dirname(__file__), 'iris_knn_model.pkl')
model = joblib.load(model_path)

st.title("🌸 Iris Flower Classifier")
st.write("Enter flower measurements below to predict the species:")

# Input sliders
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.5)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.0)

# Predict button
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    st.success(f"The predicted Iris species is **{prediction.capitalize()}**.")
