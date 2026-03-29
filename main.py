import streamlit as st
import pandas as pd
import random
import requests



import requests
import streamlit as st


OMDB_API_KEY = "864f13bf" 

def get_movie_poster(movie_title):
    """Fetches the poster URL from OMDb API"""
    
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    
    try:
        response = requests.get(url).json()
        
        if response.get('Response') == 'True' and response.get('Poster') != 'N/A':
            return response['Poster']
    except Exception as e:
        print(f"Error fetching poster: {e}")
        
    
    return "https://via.placeholder.com/500x750?text=No+Image+Found"


@st.cache_data
def load_data():
    df = pd.read_csv("clustered_movies.csv")

    df['display_title'] = df['title'] 
    df['title_lower'] = df['title'].str.lower()
    return df

df = load_data()

def recommend_movie(selected_title, n_recommendations=5):
    
    movie_row = df[df['display_title'] == selected_title]
    
    if not movie_row.empty:
        cluster = movie_row['dbscan_clusters'].values[0]
        
        if cluster == -1:
            return []

        
        cluster_movies = df[(df['dbscan_clusters'] == cluster) & (df['display_title'] != selected_title)]
        
        if len(cluster_movies) >= n_recommendations:
            recs = cluster_movies.sample(n_recommendations)['display_title'].tolist()
        else:
            recs = cluster_movies['display_title'].tolist()
        return recs
    return []


st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")
st.markdown("Using **DBSCAN Clustering** to find your next favorite watch.")

st.sidebar.header("Database Info")
st.sidebar.write("Support Databases: Netflix, HBO, Amazon")


movie_names = df['display_title'].unique()
selected_movie = st.selectbox("Type or select a movie you like:", options=movie_names)

if st.button("Get Recommendations"):
    recommendations = recommend_movie(selected_movie)
    
    if not recommendations:
        st.warning("This movie is in a unique cluster! No similar movies found.")
    else:
        st.write(f"### Because you liked **{selected_movie}**, you might enjoy:")
        
        
        cols = st.columns(5)
        
        for i, movie in enumerate(recommendations):
            with cols[i % 5]: # Use modulo to wrap if more than 5
                poster_url = get_movie_poster(movie)
                st.image(poster_url, use_container_width=True)
                st.caption(f"**{movie}**")