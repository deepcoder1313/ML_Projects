import streamlit as st
import numpy as np
import pickle

# Page settings
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

# Load model
with open("Kmeans.pkl", "rb") as f:
    model = pickle.load(f)

# Cluster labels
cluster_names = {
    0: "Daily Customer",
    1: "Weekend Customer",
    2: "Promo Customer"
}

# Sidebar
st.sidebar.title("ℹ️ About Project")
st.sidebar.write("""
This app predicts customer segments using a **KMeans Machine Learning model**.

Customer Types:
- Daily Customers
- Weekend Customers
- Promo Customers
""")

st.sidebar.write("Built with ❤️ using Python & Streamlit")

# Title
st.title("🛍️ Mall Customer Segmentation App")
st.markdown("Predict the **customer type** based on their shopping behaviour.")

st.divider()

# Layout columns
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input("👤 Age", min_value=1, max_value=100, step=1)

with col2:
    Income = st.number_input("💰 Annual Income (k$)", min_value=1, step=1)

with col3:
    Score = st.slider("🛒 Spending Score", 1, 100)

st.divider()

# Prediction button
if st.button("🔍 Predict Customer Type"):

    data = np.array([[Age, Income, Score]])

    cluster = model.predict(data)[0]

    label = cluster_names.get(cluster, "Unknown")

    st.success(f"🎯 Predicted Customer Segment: **{label}**")

    st.balloons()

st.divider()

# Footer
st.markdown("### 🚀 Built by Sandeep Singh")
st.write("Machine Learning | AI | Python Developer")