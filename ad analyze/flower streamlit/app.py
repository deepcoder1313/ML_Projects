import streamlit as st
import pandas as pd
import numpy as np
import pickle
model = pickle.load(open('flower.pkl', 'rb'))

st.title("Flower Prediction App")
file = st.file_uploader("Upload a CSV file ", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df.head())


st.subheader("Model Prediction")


id = st.number_input("Enter ID", min_value=1, max_value=150, value=1)
s_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0 )
s_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0)
p_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0)
p_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0)

def target_value(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
      features = np.array([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
      result = model.predict(features)
      return result[0]

if st.button("Predict"):
     SepalLengthCm = 5.1
     SepalWidthCm = 3.5
     PetalLengthCm = 1.4
     PetalWidthCm = 0.2
     result = target_value(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm)
     if result == "Iris-setosa":
         st.success("The predicted flower is Iris-setosa")
     elif result == "Iris-versicolor":
         st.success("The predicted flower is Iris-versicolor")
     elif result == "Iris-virginica":
         st.success("The predicted flower is Iris-virginica")
     else:
         st.error("Unknown flower species")
