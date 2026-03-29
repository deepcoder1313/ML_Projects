import pandas as pd
import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('test_score.pkl', 'rb'))

st.title('Test Score Prediction')

id = st.number_input('Enter Student ID', min_value=1, max_value=1000, value=1)
age = st.slider('Age', 10, 100, 20)
gender = st.selectbox('Gender', ['Male', 'Female'])
course  = st.text_input('Course Name')
study_hours = st.slider('Study Hours per Week', 0, 40, 10)
class_attendance = st.slider('Class Attendance (%)', 0, 100, 75)
internet_access = st.selectbox('Internet Access at Home', ['Yes', 'No'])
sleep_hours = st.slider('Sleep Hours per Night', 0, 12, 7)
sleep_quality = st.selectbox('Sleep Quality', ['Poor', 'Average', 'Good'], help='Sleep Quality (Poor, Average, Good)')
study_