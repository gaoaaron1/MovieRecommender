<template>
    <nav class="navbar">
      <router-link to="/" class="navbar-logo">
        Movies App
      </router-link>
      <ul class="nav-menu">
        <li class="nav-item">
          <router-link to="/" class="nav-links">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/movies" class="nav-links">Movies</router-link>
        </li>
      </ul>
      <div class="menu-icon">
        <i class="fas fa-bars"></i>
      </div>
    </nav>
  </template>
  
  <script>
  import './Navbar.css'; 
  
  export default {
    name: 'Navbar'
  };
  </script>
  

  