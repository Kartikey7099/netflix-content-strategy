import streamlit as st
import pandas as pd
import requests
import base64
from recommender import get_recommendations, cosine_sim
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Load data
df = pd.read_csv("netflix_data_with_cluster.csv")

# UI Configuration
st.set_page_config(page_title="Netflix Content Recommender", layout="centered")

# Netflix Logo
st.markdown(
    """
    <div style='display: flex; align-items: center; gap: 10px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg' width='100'>
        <h1 style='color: white;'>Netflix Content Recommender</h1>
    </div>
    """, unsafe_allow_html=True
)

# Dark/Light Mode Toggle
dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: white;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Filters
with st.sidebar:
    st.header("🔍 Filter Titles")
    cluster = st.selectbox("Choose a cluster (genre group):", sorted(df['cluster'].unique()))
    filtered_titles = df[df['cluster'] == cluster]['title'].dropna().sort_values().unique()
    search_title = st.selectbox("Choose a title:", filtered_titles)

# Recommend button
if st.button("📺 Recommend"):
    recommendations = get_recommendations(search_title, df, cosine_sim)
    st.subheader("Top 5 Recommendations:")
    rec_data = []

    for r in recommendations:
        poster_url = ""
        try:
            poster_url = fetch_poster(r)
        except:
            poster_url = "https://via.placeholder.com/150x220?text=No+Image"

        st.markdown(f"**{r}**")
        st.image(poster_url, width=150)
        rec_data.append([r, poster_url])

    # Download button
    if recommendations:
        df_dl = pd.DataFrame(rec_data, columns=["Title", "Poster_URL"])
        csv = df_dl.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        st.markdown(
            f'<a href="data:file/csv;base64,{b64}" download="recommendations.csv"><button>⬇️ Download CSV</button></a>',
            unsafe_allow_html=True
        )


# === Function to fetch TMDB poster ===
def fetch_poster(title):
    url = f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&query={title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path', None)
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/150x220?text=No+Image"
