from flask import Flask, request, jsonify   # Import necessary Flask modules
from flask_cors import CORS, cross_origin   # Import CORS for cross-origin requests
import pickle                              # Import pickle for loading pickled data
import requests                            # Import requests for making HTTP requests

app = Flask(__name__)                      # Initialize Flask application
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})    # Enable CORS for requests from http://localhost:5173

# Load pre-trained movie data and similarity matrix
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

#============================== API Routes =================================================

# Function to fetch movie poster path from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()       # Make GET request to TMDB API and parse JSON response
    poster_path = data['poster_path']     # Extract poster path from API response
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"   # Construct full URL for poster image

# Route to get list of movie titles 
@app.route('/movies', methods=['GET'])
def get_movies():
    movie_titles = movies['title'].tolist()   # Get list of movie titles from loaded data
    return jsonify(movie_titles)              # Return JSON response containing movie titles

# Route to recommend movies based on similarity to given movie
@app.route('/recommend', methods=['GET'])
def recommend():
    movie_title = request.args.get('title')   # Get 'title' parameter from query string
    index = movies[movies['title'] == movie_title].index[0]   # Find index of given movie title in data
    
    # Sort movies by similarity to the given movie
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []   # Initialize empty list to store recommended movies
    
    # Retrieve details and posters for top 5 similar movies
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']     # Get movie ID of recommended movie
        poster = fetch_poster(movie_id)              # Fetch poster URL using TMDB API
        recommended_movies.append({
            "name": movies.iloc[i[0]]['title'],      # Add movie title to recommended list
            "poster": poster                         # Add poster URL to recommended list
        })
    
    return jsonify(recommended_movies)    # Return JSON response with recommended movies and posters

#================================== MAIN =======================================================

if __name__ == '__main__':
    app.run(debug=True)   # Run Flask application in debug mode if executed directly
