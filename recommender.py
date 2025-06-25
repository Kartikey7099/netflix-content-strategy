import pandas as pd
import joblib
from sklearn.metrics.pairwise import linear_kernel

# Load Data
df = pd.read_csv("netflix_data_with_cluster.csv")
tfidf_matrix = joblib.load("tfidf_matrix.pkl")
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def get_recommendations(title, df, cosine_sim):
    try:
        idx = indices[title]
    except KeyError:
        return ["⚠️ Title not found in dataset."]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

__all__ = ['get_recommendations', 'cosine_sim']


