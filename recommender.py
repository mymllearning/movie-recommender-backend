# backend/recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv("dataset.csv")

movies['genre'] = movies['genre'].fillna('')
movies['overview'] = movies['overview'].fillna('')

movies['tags'] = movies['genre'] + ' ' + movies['overview']
new_df = movies[['id', 'title', 'tags']]

# Vectorization (load once)
tfidf = TfidfVectorizer(max_features=10000, stop_words='english')
vectors = tfidf.fit_transform(new_df['tags'])
similarity = cosine_similarity(vectors)

def recommend_movies(movie_name: str, top_n: int = 5):
    movie_name = movie_name.lower()
    titles = new_df['title'].str.lower()

    if movie_name not in titles.values:
        return None

    index = new_df[titles == movie_name].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )

    return [new_df.iloc[i[0]].title for i in distances[1:top_n+1]]
