<template>
    <div class="movie-card">
      <img :src="movie.poster" alt="Movie Poster" />
      <p>{{ movie.name }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ['movie']
  };
  </script>
  
  <style>
  .movie-card {
    display: inline-block;
    margin: 10px;
  }
  .movie-card img {
    width: 100px;
    height: 150px;
  }
  </style>
  