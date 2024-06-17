<template>
    <div class="app">

        <button :class="`mic ${isRecording ? 'active' : ''}`" @click="toggleMic">
            {{ isRecording ? 'Stop Recording' : 'Start Recording' }}
        </button>
        <div class="transcript" v-text="transcript"></div>
    </div>
    <div class="container">
    <header>
      <h1>Movies Recommendation System Using Machine Learning</h1>
    </header>

    <main>
      <MovieSelector :movies="movies" @recommend="getRecommendations" />
      <div v-if="recommendations.length" class="recommendations">
        <MovieCard v-for="(movie, index) in recommendations" :key="index" :movie="movie" />
      </div>
    </main>
  </div>
</template>



<script setup>
    import './Movies.css'; 
    import '../../App.css'; 

    import { ref, onMounted } from 'vue';
    import api from '../../api';
    import MovieSelector from './MovieSelector.vue';
    import MovieCard from './MovieCard.vue';
    import { transcript, isRecording, ToggleMic } from '../../voiceCommands';

    onMounted(() => {
        // Fetch movies when component is mounted
        fetchMovies();
    });

    // Reactive variables
    const movies = ref([]);
    const recommendations = ref([]);

    // Methods to interact with backend
    async function fetchMovies() {
        try {
            const response = await api.fetchMovies();
            movies.value = response.data;
        } catch (error) {
            console.error('Error fetching movies:', error);
        }
    }

    async function getRecommendations(movieTitle) {
        try {
            const response = await api.getRecommendations(movieTitle);
            recommendations.value = response.data;
        } catch (error) {
            console.error('Error getting recommendations:', error);
        }
    }

    // Function to trigger recommendations based on movie title
    function triggerRecommendation(movieTitle) {
        getRecommendations(movieTitle);
    }

    // Expose toggleMic function to template
    const toggleMic = ToggleMic;
</script>



<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Fira sans', sans-serif;
    }

    .app {
        margin-top: 20px;
        text-align: center;
    }

    .mic {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
    }

.container {
  margin-top: 20px; /* Adjust margin as needed */
  text-align: center;
}

    .mic.active {
        background-color: red;
    }

    .transcript {
        margin-top: 20px;
        font-size: 20px;
    }
</style>
