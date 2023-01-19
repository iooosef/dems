<template>
  <PrimeDialog
    v-model:visible="displayModalProp" modal="true"
    :closable="false" :draggable="false"
    class="w-fit [&>*]:!bg-white [&>*:nth-child(2)]:!rounded-t-lg [&>*:nth-child(3)]:!rounded-b-lg"
  >
    <template #header>
      <div class="flex-1 flex flex-row justify-between text-black">
        <h2 class="text-2xl font-bold">
          Select a new entry
        </h2>
      </div>
    </template>
    <div class="mt-1 grid grid-cols-2 grid-rows-2 gap-4">
      <button class="p-5 flex flex-row rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 28 28"><path fill="currentColor" d="M15.114 25.719A7.475 7.475 0 0 1 13 20.5c0-1.688.558-3.247 1.5-4.5H5a3 3 0 0 0-3 3v.715C2 23.433 6.21 26 12 26a16.81 16.81 0 0 0 3.114-.281ZM18 8A6 6 0 1 0 6 8a6 6 0 0 0 12 0Zm2.5 19a6.5 6.5 0 1 0 0-13a6.5 6.5 0 0 0 0 13Zm0-11a.5.5 0 0 1 .5.5V20h3.5a.5.5 0 0 1 0 1H21v3.5a.5.5 0 0 1-1 0V21h-3.5a.5.5 0 0 1 0-1H20v-3.5a.5.5 0 0 1 .5-.5Z" /></svg>
        <span class="ml-2">New Evacuee</span>
      </button>
      <button class="p-5 flex flex-row rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24"><path fill="currentColor" d="M17.5 12a5.5 5.5 0 1 1 0 11a5.5 5.5 0 0 1 0-11Zm0 2l-.09.007a.5.5 0 0 0-.402.402L17 14.5V17h-2.502l-.09.008a.5.5 0 0 0-.402.402l-.008.09l.008.09a.5.5 0 0 0 .402.402l.09.008H17v2.503l.008.09a.5.5 0 0 0 .402.402l.09.008l.09-.008a.5.5 0 0 0 .402-.402l.008-.09V18l2.504.001l.09-.008a.5.5 0 0 0 .402-.402l.008-.09l-.008-.09a.5.5 0 0 0-.403-.402l-.09-.008H18v-2.5l-.008-.09a.5.5 0 0 0-.402-.403L17.5 14Zm-5.478 0A6.47 6.47 0 0 0 11 17.5c0 .884.176 1.726.496 2.495C8.942 19.857 7.5 18.773 7.5 16.75v-1c0-.966.784-1.75 1.75-1.75h2.772ZM8.126 9a4.007 4.007 0 0 0 1.067 3.85l.162.151L9.25 13a2.75 2.75 0 0 0-2.649 2.008l-.034.001C3.657 15.009 2 13.919 2 11.75v-1a1.75 1.75 0 0 1 1.606-1.744L3.75 9h4.376ZM12 7a3 3 0 1 1 0 6a3 3 0 0 1 0-6Zm8.25 2c.966 0 1.75.784 1.75 1.75l-.001.962a3.4 3.4 0 0 1-.087 1.014A6.477 6.477 0 0 0 17.5 11a6.51 6.51 0 0 0-1.692.222A4.005 4.005 0 0 0 15.874 9h4.376ZM6.5 2a3 3 0 1 1 0 6a3 3 0 0 1 0-6Zm11 0a3 3 0 1 1 0 6a3 3 0 0 1 0-6Z" /></svg>
        <span class="ml-2">New Family</span>
      </button>
      <button class="p-5 flex flex-row rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24"><path fill="currentColor" d="M16 3.75a.75.75 0 0 0-.75-.75h-6.5l-.102.007A.75.75 0 0 0 8 3.75V7H6.25A3.25 3.25 0 0 0 3 10.25v6.5A3.25 3.25 0 0 0 6.25 20h11.5A3.25 3.25 0 0 0 21 16.75v-6.5A3.25 3.25 0 0 0 17.75 7H16V3.75Zm-6.5.75h5V7h-5V4.5Zm2 11.25V14H9.75a.75.75 0 0 1 0-1.5h1.75v-1.75a.75.75 0 0 1 1.5 0v1.75h1.75a.75.75 0 0 1 0 1.5H13v1.75a.75.75 0 0 1-1.5 0Z" /></svg>
        <span class="ml-2">New Medical Report</span>
      </button>
      <button class="p-5 flex flex-row rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24"><path fill="currentColor" d="M1 8.574V4.428a1.5 1.5 0 0 1 .83-1.342l3.5-1.75a1.5 1.5 0 0 1 1.34 0l3.5 1.75A1.5 1.5 0 0 1 11 4.428v4.146a1.5 1.5 0 0 1-.83 1.341l-3.5 1.75a1.5 1.5 0 0 1-1.34 0l-3.5-1.75A1.5 1.5 0 0 1 1 8.574Zm1.553-4.047a.5.5 0 0 0 .223.67L5.5 6.56V9.5a.5.5 0 1 0 1 0V6.56l2.724-1.362a.5.5 0 1 0-.448-.895L6 5.692L3.224 4.303a.5.5 0 0 0-.671.224Zm9-1.527A2.5 2.5 0 0 1 12 4.428v4.145a2.5 2.5 0 0 1-1.382 2.236l-3.5 1.75a2.5 2.5 0 0 1-2.236 0L2 11.12v6.131a2.25 2.25 0 0 0 2.04 2.24a3 3 0 0 0 5.919.01h2.082a3 3 0 0 0 5.918 0h1.791A2.25 2.25 0 0 0 22 17.25v-5.412a2.25 2.25 0 0 0-.217-.963l-1.699-3.588A2.25 2.25 0 0 0 18.051 6H16.5v-.75A2.25 2.25 0 0 0 14.25 3h-2.697Zm7.697 12.5h1.25V17h-1.25a.75.75 0 1 1 0-1.5Zm-.521-7.57L20.183 11H16.5V7.5h1.55a.75.75 0 0 1 .679.43ZM8.5 19a1.5 1.5 0 1 1-3 0a1.5 1.5 0 0 1 3 0Zm6.5-1.5a1.5 1.5 0 1 1 0 3a1.5 1.5 0 0 1 0-3Z" /></svg>
        <span class="ml-2">New Relief Operation</span>
      </button>
    </div>
  </PrimeDialog>
</template>

<script>
import { ref } from 'vue'
import PrimeDialog from 'primevue/dialog'

export default {
  name: 'NewEntryModal',
  components: {
    PrimeDialog
  },
  props: {
    displayModal: {
      type: Boolean,
      required: true
    }
  },
  setup (props) {
    const displayModalProp = ref(props.displayModal)
    return { ...props, displayModalProp }
  }
}
</script>
export default {
    name: 'NewEntryModal'
}

<style lang="scss" scoped>

</style>
