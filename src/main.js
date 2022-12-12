import { createApp } from 'vue'
import App from './App.vue'

import vSelect from "vue-select"
import "bootstrap/dist/js/bootstrap.js"
import Dropdown from 'primevue/dropdown';

// styles import
import "./assets/css/Main.css"
import "bootstrap/dist/css/bootstrap.css"
import "vue-select/dist/vue-select.css"
import "primevue/resources/themes/lara-light-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})

const app = createApp({});    
app.component('Dropdown', Dropdown);
app.component("vSelect", vSelect);



createApp(App).use(vuetify).mount('#app');


