import pandas as pd
import numpy as np
import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Define these OUTSIDE the function to save processing time
STOP_WORDS = set(stopwords.words("english"))
STEMMER = PorterStemmer()


with open('model.pkl', 'rb') as f:
    rfc = pickle.load(f)
with open('tfid_vect', 'rb') as f:
    tfid = pickle.load(f)



def clean_text(text):
    text = text.lower()

    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
   
    text = re.sub(r'[^a-z\s]', '', text)
    words = word_tokenize(text)

    cleaned_words = [STEMMER.stem(w) for w in words if w not in STOP_WORDS]

    return " ".join(cleaned_words)



def detection(text):
    cleaned_text = clean_text(text)
    vector_text = tfid.transform([cleaned_text])
    result = rfc.predict(vector_text)
    return result
    
st.title("Fake Spam Detection")
input_text = st.text_area("Enter the text to analyze:")
if st.button("Detect"):
    if not input_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner('Analyzing text...'):
            prediction = detection(input_text)
            
        if prediction[0] == 1:
            st.error("🚨 This looks like SPAM.")
        else:
            st.success("✅ This looks LEGIT.")