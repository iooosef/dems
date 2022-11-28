import Vue from 'vue'
import { createApp } from 'vue'
import App from './App.vue'

Vue.prototype.$eel = window.eel;
createApp(App).mount('#app')
