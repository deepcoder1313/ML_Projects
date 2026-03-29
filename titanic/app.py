import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")

st.title("Titanic Survival Predictor")
st.write("Enter the details of the passenger to predict survival on the Titanic.")

pclass = st.selectbox("Passenger Class ", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Number of Parents/Children Aboard", min_value=0, max_value=10, value=0)
Embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

family_size = sibsp + parch + 1

input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'SibSp': [sibsp],
    'Parch': [parch],
    'Embarked': [Embarked],
    "FamilySize" : [family_size]
})

if st.button("Predict Survival"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("The passenger is predicted to have survived.")
    else:
        st.error("The passenger is predicted to have not survived.")