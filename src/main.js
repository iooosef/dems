import { createApp } from 'vue'
import App from './App.vue'

import vSelect from "vue-select"
import "bootstrap/dist/js/bootstrap.js"

// styles import
import "./assets/css/Main.css"
import "bootstrap/dist/css/bootstrap.css"
import "vue-select/dist/vue-select.css"

const app = createApp({});

app.component("vSelect", vSelect);

createApp(App).mount('#app');


