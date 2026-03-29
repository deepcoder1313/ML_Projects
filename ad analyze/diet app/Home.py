import streamlit as st

st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(to top, #30cfd0 0%, #330867 100%);
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("🥗 Welcome to Diet Prediction App")
st.subheader("◀  Use the sidebar to navigate between pages.")

st.image("https://i.pinimg.com/originals/69/33/f6/6933f66e103ac858650368335e7a0d39.gif")



