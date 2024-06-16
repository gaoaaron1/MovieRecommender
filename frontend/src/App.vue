<script>
import api from './api';
import MovieSelector from './components/MovieSelector.vue';
import MovieCard from './components/MovieCard.vue';


export default {
  name: 'App',
  components: {
    MovieSelector,
    MovieCard,
  },
  data() {
    return {
      movies: [],
      recommendations: [],
    };
  },
  methods: {
    async fetchMovies() {
      try {
        const response = await api.fetchMovies();
        this.movies = response.data;
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    },
    async getRecommendations(movieTitle) {
      try {
        const response = await api.getRecommendations(movieTitle);
        this.recommendations = response.data;
      } catch (error) {
        console.error('Error getting recommendations:', error);
      }
    },
  },
  created() {
    this.fetchMovies();
  },
};


import { ref, onMounted } from 'vue'
const transcript = ref('')
const isRecording = ref(false)

const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition
const sr = new Recognition()

onMounted(() => {
	sr.continuous = true
	sr.interimResults = true

	sr.onstart = () => {
		console.log('SR Started')
		isRecording.value = true
	}

	sr.onend = () => {
		console.log('SR Stopped')
		isRecording.value = false
	}

	sr.onresult = (evt) => {
		for (let i = 0; i < evt.results.length; i++) {
			const result = evt.results[i]

			if (result.isFinal) CheckForCommand(result)
		}

		const t = Array.from(evt.results)
			.map(result => result[0])
			.map(result => result.transcript)
			.join('')
			.toLowerCase(); // Convert to lowercase

		transcript.value = t
	}
})

const CheckForCommand = (result) => {
	const t = result[0].transcript.toLowerCase();
	console.log(t);
	if (t.includes('stop recording' || 'stop recording.')) {
		sr.stop()
	} else if (
		t.includes('what is the time') ||
		t.includes('what\'s the time')
	) {
		sr.stop()
		alert(new Date().toLocaleTimeString())
		setTimeout(() => sr.start(), 100)
	}
}

const ToggleMic = () => {
	if (isRecording.value) {
		sr.stop()
	} else {
		sr.start()
	}
}
</script>

<template>
	<div class="app">
		<button :class="`mic`" @click="ToggleMic">Record</button>
		<div class="transcript" v-text="transcript"></div>
	</div>


	
	<header>
		<h1>Movies Recommendation System Using Machine Learning</h1>
	</header>

	
	<main>
		<MovieSelector :movies="movies" @recommend="getRecommendations" />
		<div v-if="recommendations.length" class="recommendations">
		<MovieCard v-for="(movie, index) in recommendations" :key="index" :movie="movie" />
		</div>
	</main>
	



</template>

<style>
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Fira sans', sans-serif;
}

body {
	background: #281936;
	color: #FFF;
}
</style>