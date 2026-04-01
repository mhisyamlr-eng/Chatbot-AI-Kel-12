import requests

API_KEY = "c19ee3170938aba50a617ed881daa2c7"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {"query": title, "api_key": API_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
    return None


def get_movie_details(movie_id):
    # Get genres
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY}
    response = requests.get(url, params=params)

    genres = []
    if response.status_code == 200:
        genres = [g["name"] for g in response.json().get("genres", [])]

    # Get cast
    credits_url = f"{BASE_URL}/movie/{movie_id}/credits"
    credits_res = requests.get(credits_url, params=params)

    cast = []
    if credits_res.status_code == 200:
        cast = [actor["name"] for actor in credits_res.json().get("cast", [])[:5]]

    return genres, cast


def format_movie_info(movie):
    movie_id = movie["id"]
    genres, cast = get_movie_details(movie_id)

    poster_path = movie.get("poster_path")
    poster_url = IMAGE_BASE + poster_path if poster_path else ""

    return f"""
## 🎬 {movie['title']} ({movie.get('release_date', 'N/A')[:4]})

![poster]({poster_url})

⭐ **Rating:** {movie.get('vote_average', 'N/A')}/10  

🎭 **Cast:** {", ".join(cast) if cast else "N/A"}  

🎬 **Genre:** {", ".join(genres) if genres else "N/A"}  

📖 **Overview:**  
{movie.get('overview', 'No description available.')}

💬 *What do you think about this movie? Want recommendations like this?*
"""
