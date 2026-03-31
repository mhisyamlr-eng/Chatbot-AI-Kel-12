import requests
import os

API_KEY = "c19ee3170938aba50a617ed881daa2c7"
BASE_URL = "https://api.themoviedb.org/3"
def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {"query": title, "api_key": API_KEY}
    response = requests.get(url, params=params)   # This is the API call
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]   # Return the top matching result
    return None
def format_movie_info(movie):
    return (
        f"🎬 **{movie['title']}** ({movie.get('release_date', 'N/A')[:4]})\n\n"
        f"⭐ Rating: {movie.get('vote_average', 'N/A')}/10\n\n"
        f"📖 {movie.get('overview', 'No description available.')}"
    )