import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// plugin imports
import PrimeVue from 'primevue/config'
import Toast from 'primevue/toast'
import ToastService from 'primevue/toastservice'
import PrimeDialog from 'primevue/dialog'
// css imports
import './index.css'
import 'primevue/resources/themes/tailwind-light/theme.css'
import 'primevue/resources/primevue.min.css'
import 'primeicons/primeicons.css'

const app = createApp(App)
app.use(router)
app.use(PrimeVue, {
  zIndex: {
    modal: 1000
  }
})
app.use(ToastService)
app.component('PrimeToast', Toast)
app.component('PrimeDialog', PrimeDialog)

app.mount('#app')
