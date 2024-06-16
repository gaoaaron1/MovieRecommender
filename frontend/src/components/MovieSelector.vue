<template>
    <div>
      <select v-model="selectedMovie" @change="recommend" class="custom-select">
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
  
  <style scoped>
.custom-select {
  width: 300px; /* Adjust the width as per your design */
  padding: 8px; /* Optional: Adjust padding for better appearance */
}
</style>