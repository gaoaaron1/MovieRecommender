<template>
  <div class="container">
    <select v-model="selectedMovieLocal" @change="emitRecommend" class="custom-select">
      <option v-for="movie in movies" :key="movie" :value="movie">{{ movie }}</option>
    </select>
    <button @click="emitRecommend">Show recommendation</button>
  </div>
</template>

<script>
import './MovieSelector.css';
export default {
  props: ['movies', 'selectedMovie'],
  data() {
    return {
      selectedMovieLocal: this.selectedMovie
    };
  },
  watch: {
    selectedMovie(newVal) {
      this.selectedMovieLocal = newVal;
      this.recommend();
    }
  },
  methods: {
    emitRecommend() {
      this.$emit('recommend', this.selectedMovieLocal);
    },
    recommend() {
      this.$emit('recommend', this.selectedMovieLocal);
    }
  }
};
</script>

<style scoped>
.custom-select {
  width: 300px; /* Adjust the width as per your design */
  padding: 8px; /* Optional: Adjust padding for better appearance */
}
</style>
