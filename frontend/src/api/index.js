import axios from 'axios';

const API = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL, // Use the environment variable
});

export default {
  fetchMovies() {
    return API.get('/movies');
  },
  getRecommendations(movieTitle) {
    return API.get(`/recommend?title=${movieTitle}`);
  },
};
