import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],
  build: {
    outDir: 'dist'  // Ensures Vite outputs to the 'dist' directory
  },
  define: {
    'process.env': process.env
  }
});
