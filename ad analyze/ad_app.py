import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open('ad_sales_model.pkl', 'rb'))

st.title('📺 Advertisement Sales Prediction')

st.write("Enter advertisement budget to predict sales")

# Numeric inputs (SAFE)
tv = st.number_input('TV Ad Budget ($)')
radio = st.number_input('Radio Ad Budget ($)')
newspaper = st.number_input('Newspaper Ad Budget ($)')

if st.button('Predict Sales'):
    features = np.array([[tv, radio, newspaper]])
    result = model.predict(features)
    st.success(f'📈 Predicted Sales: {result[0]:.2f}')
