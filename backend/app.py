from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://movie-recommender-frontend-alpha.vercel.app"]}})  # Update with your frontend URL

# Load pre-trained movie data and similarity matrix
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# Function to fetch movie poster path from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"

# Route to get list of movie titles 
@app.route('/movies', methods=['GET'])
def get_movies():
    movie_titles
