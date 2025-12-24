from fastapi import FastAPI, HTTPException,Query
from pydantic import BaseModel
from recommender import recommend_movies,new_df
from tmdb import get_movie_poster

app = FastAPI(title="Movie Recommendation API")

class MovieRequest(BaseModel):
    movie_name: str

@app.post("/recommend")
def recommend(request: MovieRequest):
    recommendations = recommend_movies(request.movie_name)

    if not recommendations:
        raise HTTPException(status_code=404, detail="Movie not found")

    movies = []
    for movie in recommendations:
        movies.append({
            "title": movie,
            "poster": get_movie_poster(movie)
        })

    return {
        "input_movie": request.movie_name,
        "recommendations": movies
    }


@app.get("/autocomplete")
def autocomplete(
    q: str = Query(..., min_length=1),
    limit: int = 8
):
    q = q.lower()

    matches = (
        new_df[new_df['title'].str.lower().str.contains(q)]
        ['title']
        .head(limit)
        .tolist()
    )

    return {
        "query": q,
        "results": matches
    }