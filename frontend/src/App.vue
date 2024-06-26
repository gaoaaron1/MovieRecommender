<template>
	<div id="app">
	  <Navbar />
    <ChatBox />
	  <router-view />
	</div>
  </template>
  
  <script>
  import Navbar from './components/Navbar/Navbar.vue';
  import ChatBox from './components/ChatBox.vue';

  export default {
	name: 'App',
	components: {
    ChatBox,
	  Navbar
	},
  };
  </script>
  
  <style>
  /* Your global styles */
  </style>
  