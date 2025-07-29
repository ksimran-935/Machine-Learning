# 🚗 Car Resale Price Estimator

A Streamlit web application that predicts the **selling price of a used car** based on its specifications like mileage, engine size, fuel type, transmission, and more.

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Available-brightgreen?logo=streamlit)](https://machine-learning-hlnzzgwgugh33ovwcenltq.streamlit.app/)


---
## 🧩 Problem Statement

Estimating the resale value of a used car can be a complex process influenced by many factors such as age, distance driven, fuel type, and power. Car sellers often struggle to determine a fair price, and buyers want to ensure they're paying the right amount.

**Goal**:  
To build a machine learning-powered web application that predicts the **resale price of a car** using its features. This empowers users—sellers, buyers, or dealers—to make informed decisions backed by data.

---

## 📌 Features

- 🧠 **Machine Learning Powered**: Uses a trained Random Forest Regressor model.
- 🧾 **User Inputs**: Collects car specs like vehicle age, fuel type, power, mileage, etc.
- ⚙️ **Dynamic Prediction**: Calculates and displays estimated price in real-time.
- 💾 **Model Hosting via Google Drive**: Model too large for GitHub? It's downloaded at runtime from Drive.
- 🌐 **Deployed on Streamlit Cloud**: Runs fully online, no local setup needed.

---

## 🚀 How It Works

The app takes input from the user through dropdowns and sliders, formats the data with one-hot encoding, and feeds it to a pre-trained machine learning model to predict the car's resale price.

---

## 🧠 Model Details

- **Algorithm**: Random Forest Regressor
- **Trained On**: Cleaned and processed used car dataset
- **Preprocessing**: One-hot encoding for categorical variables, feature scaling handled during training

---

## 🛠 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Joblib](https://joblib.readthedocs.io/)

---

## 📦 Files in this Repo

| File                | Description                                   |
|---------------------|-----------------------------------------------|
| `app.py`            | Main Streamlit app source code                |
| `requirements.txt`  | Python dependencies                           |
| `Car_Prediction.ipynb`       | Source code            |
| `README.md`         | You're reading it                             |

---

## 📁 Model Download via Google Drive

Since the trained model file is too large for GitHub, it's stored on **Google Drive** and automatically downloaded when the app first runs.

**Drive Link Used**: [Random Forest Model](https://drive.google.com/file/d/1ziYd-KdiGqeyCl38LK7m19MaiEoemSIX/view?usp=sharing)

---

## ✅ How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/car-price-estimator.git
cd car-price-estimator
pip install -r requirements.txt
streamlit run app.py
