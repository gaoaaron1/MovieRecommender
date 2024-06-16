<template>
    <div>
      <select v-model="selectedMovie" @change="recommend">
        <option v-for="movie in movies" :key="movie" :value="movie">{{ movie }}</option>
      </select>
      <button @click="recommend">Show recommendation</button>
    </div>
  </template>
  
  <script>
  export default {
    props: ['movies'],
    data() {
      return {
        selectedMovie: ''
      };
    },
    methods: {
      recommend() {
        this.$emit('recommend', this.selectedMovie);
      }
    }
  };
  </script>
  