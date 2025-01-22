import requests
import random

# TMDb API base URL and API key
API_KEY = "YOUR_API_KEY"  # Replace with your TMDb API Key
BASE_URL = "https://api.themoviedb.org/3"
GENRES_URL = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
MOVIES_URL = f"{BASE_URL}/discover/movie?api_key={API_KEY}&language=en-US&with_genres="

# Function to fetch genres
def fetch_genres():
    try:
        response = requests.get(GENRES_URL)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['genres']
        else:
            print(f"Error fetching genres: {response.status_code}")
            print("Response message:", response.json())
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching genres: {e}")
        return []

# Function to fetch movies by genre
def fetch_movies_by_genre(genre_id):
    try:
        url = MOVIES_URL + str(genre_id)
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['results']
        else:
            print(f"Error fetching movies: {response.status_code}")
            print("Response message:", response.json())
            return []
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching movies: {e}")
        return []

# Function to recommend a random movie from a genre
def recommend_movie():
    genres = fetch_genres()

    if not genres:
        return

    # Display available genres
    print("Available movie genres:")
    for index, genre in enumerate(genres, 1):
        print(f"{index}. {genre['name']}")

    # Ask the user to select a genre
    try:
        genre_choice = int(input("\nPlease enter the number of the genre you want: "))
        if genre_choice < 1 or genre_choice > len(genres):
            print("Invalid choice. Please select a valid genre number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Get the genre ID
    selected_genre = genres[genre_choice - 1]
    genre_id = selected_genre['id']

    # Fetch movies from the selected genre
    movies = fetch_movies_by_genre(genre_id)

    if not movies:
        print("No movies found for this genre.")
        return

    # Recommend a random movie
    random_movie = random.choice(movies)
    movie_title = random_movie['title']
    movie_overview = random_movie['overview']

    print(f"\nRecommended Movie: {movie_title}")
    print(f"Overview: {movie_overview}\n")

if __name__ == "__main__":
    recommend_movie()
