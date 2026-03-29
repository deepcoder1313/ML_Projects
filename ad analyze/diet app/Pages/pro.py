import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt



model = joblib.load("../pro_predict1.pkl")


st.title("🥗 Diet Nutrient Predictor")






st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
       background-image: linear-gradient(to right, #434343 0%, black 100%);
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


calories_input = st.sidebar.number_input(" 🧘‍♀️ Enter your Calories", min_value=0, value=2000, step=50)

def predict_nutrients(calories):
    input_df = pd.DataFrame({"Recommended_Calories": [calories]})
    prediction = model.predict(input_df)
    return prediction[0]  # [Protein, Fats, Carbs]

if st.sidebar.button("Predict"):
    protein, fats, carbs = predict_nutrients(calories_input)
    
    # Show results
    st.subheader("Predicted Nutrients")


    st.sidebar.success(f"Protein: {protein:.2f} g 🔥")
   

    st.sidebar.info(f"Fats: {fats:.2f} g 🥑")
    st.sidebar.warning(f"Carbs: {carbs:.2f} g 🍐")
    


    labels = ["Protein", "Fats", "Carbs"]
    values = [protein, fats, carbs]
    colors = ["#ff9999", "#66b3ff", "#99ff99"]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    ax.axis("equal")  
    plt.title(" Nutrients Distribution")
    plt.legend()
    st.pyplot(fig)
