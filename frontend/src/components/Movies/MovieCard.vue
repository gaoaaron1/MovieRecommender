<template>
    <div class="movie-card">
      <img :src="movie.poster" alt="Movie Poster" />
      <p>{{ movie.name }}</p>
    </div>

  </template>
  
  <script>
  import './MovieCard.css';

  export default {
    props: ['movie']
  };
  </script>
  



  <style>
.movie-card {
  display: inline-block;
  margin: 10px;
  text-align: center; /* Center-align content */
  width: 150px; /* Fixed width for each card */
}

.movie-card img {
  width: 100px;
  height: 150px;
  display: block; /* Ensure the image does not affect vertical alignment */
  margin: 0 auto; /* Center the image horizontally */
}

.movie-card p {
  margin-top: 5px; /* Space between image and movie name */
  margin-bottom: 0; /* Remove default margin */
  overflow: hidden; /* Ensure text doesn't overflow */
  text-overflow: ellipsis; /* Show ellipsis if text is too long */
  white-space: nowrap; /* Prevent wrapping */
}

</style>
  