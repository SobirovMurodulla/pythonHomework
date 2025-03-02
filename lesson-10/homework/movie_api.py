import requests
import random
import textwrap

# Replace 'your_api_key' with your actual TMDb API key
api_key = 'a6ef8aa9a5fa4c597e563f57bb7d8d4c'
base_url = 'https://api.themoviedb.org/3'

def get_genres(api_key):
    url = f"{base_url}/genre/movie/list"
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        genres = response.json()['genres']
        return {genre['name']: genre['id'] for genre in genres}
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return {}

def get_movies_by_genre(api_key, genre_id):
    url = f"{base_url}/discover/movie"
    params = {'api_key': api_key, 'with_genres': genre_id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        movies = response.json()['results']
        return movies
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

def recommend_movie(api_key, genre_name):
    genres = get_genres(api_key)
    if genre_name in genres:
        genre_id = genres[genre_name]
        movies = get_movies_by_genre(api_key, genre_id)
        if movies:
            movie = random.choice(movies)
            print(f"Recommended Movie: {movie['title']}")
            print("Overview:")
            print(textwrap.fill(movie['overview'], width=70))
        else:
            print("No movies found for this genre.")
    else:
        print("Genre not found.")

if __name__ == "__main__":
    genre_name = input("Enter a movie genre: ")
    recommend_movie(api_key, genre_name)