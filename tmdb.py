import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def get_movie_poster(movie_name: str):
    search_url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name
    }

    response = requests.get(search_url, params=params).json()

    if response["results"]:
        poster_path = response["results"][0].get("poster_path")
        if poster_path:
            return IMAGE_BASE + poster_path

    return None
