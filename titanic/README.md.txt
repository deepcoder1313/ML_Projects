# Titanic Survival Prediction

This is an end-to-end machine learning project that predicts whether a passenger survived the Titanic disaster.

## Project Overview
The goal of this project is to build a machine learning model that predicts survival using passenger data such as age, gender, class, fare, and family size.

## Features Used
- Pclass  
- Sex  
- Age  
- SibSp  
- Parch  
- Fare  
- Embarked  
- FamilySize  

## Workflow
- Data cleaning and preprocessing  
- Feature engineering (FamilySize)  
- Handling missing values  
- Encoding categorical variables  
- Model training using Logistic Regression  
- Model evaluation  
- Kaggle submission file creation  
- Model saving using pickle  
- Streamlit app for predictions  

## Files in this Project
- `train.csv` – Training dataset  
- `test.csv` – Test dataset  
- `submission.csv` – Kaggle submission file  
- `titanic_model.pkl` – Trained ML model  
- `app.py` – Streamlit app code  
- `README.md` – Project description  

## How to Run the App

```bash
streamlit run app.py
