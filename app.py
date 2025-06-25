import streamlit as st
import pandas as pd
from recommender import get_recommendations, cosine_sim

# Load Data
df = pd.read_csv("netflix_data_with_cluster.csv")

# UI Setup
st.set_page_config(page_title="Netflix Content Recommender", layout="centered")
st.title("🎬 Netflix Content Recommender")
st.write("Enter a title and get similar content recommendations.")

# Title Selection
title = st.selectbox("Choose a title:", df['title'].dropna().sort_values().unique())

# Recommendation Trigger
if st.button("Recommend"):
    recs = get_recommendations(title, df, cosine_sim)
    st.subheader("Top 5 Recommendations:")
    for r in recs:
        st.write(f"📺 {r}")
