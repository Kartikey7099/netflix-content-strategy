# app.py

import streamlit as st
import pandas as pd
import joblib
from recommender import get_recommendations

# Load Data
df = pd.read_csv("netflix_data_with_cluster.csv")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")

# Build UI
st.set_page_config(page_title="Netflix Content Recommender", layout="centered")
st.title("🎬 Netflix Content Recommender")
st.write("Enter a title and get similar content recommendations.")

title = st.selectbox("Choose a title:", df['title'].dropna().sort_values().unique())

if st.button("Recommend"):
    recs = get_recommendations(title, df, tfidf_matrix)
    st.subheader("Top 5 Recommendations:")
    for r in recs:
        st.write(f"📺 {r}")
