import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Home from './components/Home/Home.vue';
import Movies from './components/Movies/Movies.vue'; 

//Navigation routes
const routes = [
  { path: '/', component: Home },
  { path: '/movies', component: Movies }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

createApp(App)
  .use(router)
  .mount('#app');
