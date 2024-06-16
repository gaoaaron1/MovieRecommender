import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000', // Adjust the base URL as needed
});

export default {
  fetchMovies() {
    return API.get('/movies');
  },
  getRecommendations(movieTitle) {
    return API.get(`/recommend?title=${movieTitle}`);
  },
};
