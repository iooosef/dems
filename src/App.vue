<template>
  <MainApp />
</template>

<script>
import MainApp from './components/Main.vue'

export default {
  name: 'App',
  components: {
    MainApp
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    height: 100%;
    width: 100%;
  }

  main {
      height: 99.9vh;
  }

  nav {
      height: 60px;
  }

  section {
      height: calc(100% - 60px);
  }

  h1, h2, h3, h4, h5, h6 {
      margin-bottom: 0;
      line-height: 1.8;
  }

  /* bootstrap override */
  :root {
    --bs-border-radius-lg2: 0.8rem;
  }

  .bg-light-gray {
    --bs-bg-opacity: 1;
    background-color: var(--bs-gray-100) !important;
  }

  .mb-4b,
  .my-4b {
    margin-bottom: 2rem !important;
  }

  .p-4b {
  padding: 2rem !important;
  }

  .row {
    --bs-gutter-x: 0;
  }

  .rounded-3b {
    border-radius: var(--bs-border-radius-lg2) !important;
  }

  .rounded-start-3b {
    border-bottom-left-radius: var(--bs-border-radius-lg2) !important;
    border-top-left-radius: var(--bs-border-radius-lg2) !important;
  } .rounded-end-3b {
    border-top-right-radius: var(--bs-border-radius-lg2) !important;
    border-bottom-right-radius: var(--bs-border-radius-lg2) !important;
  }

  .rounded-start-0 {
    border-bottom-left-radius: 0 !important;
    border-top-left-radius: 0 !important;
  } .rounded-end-0 {
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important;
  }  
</style>
