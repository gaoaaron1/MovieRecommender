from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import requests

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"

@app.route('/movies', methods=['GET'])
def get_movies():
    movie_titles = movies['title'].tolist()
    return jsonify(movie_titles)

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_title = request.args.get('title')
    index = movies[movies['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        poster = fetch_poster(movie_id)
        recommended_movies.append({"name": movies.iloc[i[0]].title, "poster": poster})
    
    return jsonify(recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
