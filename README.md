
# 🎬 Netflix Content Strategy Recommender

A Machine Learning + NLP project that analyzes Netflix content trends and provides personalized title recommendations based on content descriptions and genres.

## 📊 Project Overview

This project reverse-engineers Netflix's content strategy by:
- Analyzing what genres and descriptions attract viewers
- Clustering similar shows/movies
- Recommending related content using cosine similarity

The model uses **TF-IDF Vectorization** and **KMeans Clustering**, and is deployed as an interactive web app using **Streamlit**.

---

## 💡 Key Features

- 🔍 Explore Netflix content trends
- 📈 Cluster-based content similarity
- 🎯 Title-based recommendation system
- 🖥️ Deployed Streamlit web app

---

## 🚀 Try the App

👉 [Live Demo on Streamlit Cloud](https://your-app-link.streamlit.app)  
*(Replace with your actual Streamlit URL once deployed)*

---

## 🛠️ Tech Stack

| Area | Tools/Tech |
|------|------------|
| Programming | Python |
| Data | Pandas, CSV |
| NLP | Scikit-learn (TF-IDF), KMeans |
| Deployment | Streamlit Cloud |
| Model Storage | joblib (pickle format) |

---

## 📁 Project Structure

```
netflix-content-strategy/
├── app.py                  # Streamlit app
├── recommender.py          # Recommendation engine
├── netflix_titles.csv      # Netflix dataset
├── tfidf.pkl               # Saved TF-IDF vectorizer
├── tfidf_matrix.pkl        # Transformed features
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/netflix-content-strategy.git
cd netflix-content-strategy
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📚 Dataset

Netflix titles dataset sourced from:  
[Netflix Titles on Kaggle](https://www.kaggle.com/shivamb/netflix-shows)

---

## 🧠 Learnings

- Applied TF-IDF on mixed-text metadata (genre + description)
- Implemented cosine similarity for content-based filtering
- Created deployable ML product with Streamlit

---

## 📩 Contact

Made with ❤️ by [Your Name]  
📧 Email: your.email@example.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yourprofile)
