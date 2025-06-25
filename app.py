import streamlit as st
import pandas as pd
import joblib
from recommender import get_recommendations

df = pd.read_csv("netflix_titles.csv")
tfidf = joblib.load("tfidf.pkl")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")

st.title("🎬 Netflix Content Recommender")
st.write("Enter a title and get similar content recommendations.")

title = st.selectbox("Choose a title:", df['title'].dropna().unique())

if st.button("Recommend"):
    recs = get_recommendations(title, df, tfidf_matrix)
    st.subheader("Recommended Titles:")
    for r in recs:
        st.write("•", r)
