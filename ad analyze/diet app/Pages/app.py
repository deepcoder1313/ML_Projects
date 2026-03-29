import streamlit as st
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import cloudpickle
with open("../model_pipeline0.pkl", "rb") as f:
    model_pipeline = cloudpickle.load(f)


with open("../diet0.pkl", "rb") as f:
    model_pipeline = cloudpickle.load(f)

    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://previews.123rf.com/images/peangdao/peangdao1411/peangdao141100064/33644418-healthy-food-background.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown("""
    <div style='text-align: center; padding: 10px;  border-radius: 10px;background-color:#E8FFD8 ;opacity: 0.7'>
        <h1 style='color: Black; font-size: 40px'>🥗 Customized Diet Plan Predictor</h1>
    </div>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
     background-image: linear-gradient(to top, #a7a6cb 0%, #8989ba 52%, #8989ba 100%);
                color: black;
    }
    [data-testid="stSidebar"] .stTextInput > div > div > input {
        color: white;
    }
    [data-testid="stSidebar"] label {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.header("Enter your Detail 💬")

age =st.sidebar.number_input("📆 Age")
Gender =st.sidebar.selectbox("♂️ Gender",
                             options=["Male", "Female"]
                             )
height = st.sidebar.number_input("🧍↕ Height (cm)")
weight = st.sidebar.number_input("🧘🏻‍♀️ Weight (kg)")
activity_level = st.sidebar.selectbox(
    "🚀 Activity level",
    options=["Sedentary", "Lightly active", "Moderately active", "High", "Extra active"]
)

goal = st.sidebar.selectbox( "Main Goal",
     options=['⏳ Lose','💪🏻 Gain','🔋 Maintain']

                             )
bmr=st.sidebar.number_input("📈 BMR")
td =st.sidebar.number_input("🎯 TDEE")


if st.sidebar.button(" SUBMIT "):
    

    input_df = pd.DataFrame({
        "Age": [age],
        "Gender": [Gender],
        "Height_cm": [height],
        "Weight_kg": [weight],
        "Activity_Level": [activity_level],

        "Goal": [goal],
        "BMR": [bmr],
        "TDEE": [td]
    })

    predicted_calories = model_pipeline.predict(input_df)[0]



    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; padding: 8px; border-radius: 10px;'>
            <h1 style='color: #fff; font-size: 35px; text-shadow: 2px 2px 4px #000;'>🔥 Predicted Calories Needed:</h1>
        </div>
    """, unsafe_allow_html=True)
    # Example replacement for st.success()
\
    st.markdown(
        f"""
        <div style='
            background-color: rgba(0, 255, 0, 0.1);
            color: green;
            padding: 1.2rem;
            border-radius: 12px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            opacity: 0.9;
        '>
            🔥 {round(predicted_calories, 2)} calories/day
        </div>
        """,
        unsafe_allow_html=True
        
    )
st.image("https://i.pinimg.com/originals/cc/52/d8/cc52d88c5738d491c2175c408d90d1dc.gif",width=600)


