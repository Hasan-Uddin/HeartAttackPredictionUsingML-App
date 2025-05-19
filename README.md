# 💓 Heart Attack Risk Predictor

A machine learning-powered web application that predicts a patient's risk of having a heart attack based on key clinical parameters.

## 🧠 Project Overview

This application takes in medical inputs such as age, blood pressure, heart rate, and cardiac enzyme levels to estimate the likelihood of a heart attack using a trained Random Forest model. The web interface is built using Streamlit.

## 📁 Folder Structure

project/
├── app.py
├── model/
│ └── heart_model.pkl
├── assets/
│ ├── heart.png
│ └── caption.png


## 🧪 Features

- User-friendly web interface
- Real-time prediction of heart attack risk
- Model trained using:
  - Age
  - Gender
  - Heart rate
  - Systolic & Diastolic blood pressure
  - Blood sugar
  - CK-MB & Troponin levels

## 📊 Dataset

Sourced from [Kaggle](https://www.kaggle.com/datasets/fatemehmohammadinia/heart-attack-dataset-tarik-a-rashid), the dataset includes clinical data points relevant to heart health.

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/heart_attack_predictor.git
cd heart_attack_predictor
2. Install dependencies
