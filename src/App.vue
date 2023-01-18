<template>
  <div class="flex flex-row h-screen bg-white">
    <nav class="w-60 p-5 bg-white drop-shadow-border z-20">
      <img src="@/assets/img/logo.png" alt="Disaster Evacuees Management System logo" class="w-full">
      <div class="w-full mt-5 px-3 py-5 flex flex-row bg-primary-500 rounded-lg text-2xl text-white font-semibold hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer" tabindex="1">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path fill="currentColor" d="M16 30c7.732 0 14-6.268 14-14S23.732 2 16 2S2 8.268 2 16s6.268 14 14 14Zm-1-19a1 1 0 1 1 2 0v4h4a1 1 0 1 1 0 2h-4v4a1 1 0 1 1-2 0v-4h-4a1 1 0 1 1 0-2h4v-4Z" /></svg>
        <span class="ml-2">New Entry</span>
      </div>
      <div class="w-full mt-4 p-3 flex flex-row bg-light-500 rounded-lg text-xl text-black font-semibold hover:bg-light-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500 transition duration-200 cursor-pointer" tabindex="2">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M17.754 14a2.249 2.249 0 0 1 2.249 2.25v.918a2.75 2.75 0 0 1-.513 1.598c-1.545 2.164-4.07 3.235-7.49 3.235c-3.421 0-5.944-1.072-7.486-3.236a2.75 2.75 0 0 1-.51-1.596v-.92A2.249 2.249 0 0 1 6.251 14h11.502ZM12 2.005a5 5 0 1 1 0 10a5 5 0 0 1 0-10Z" /></svg>
        <span class="ml-2">Evacuees</span>
      </div>
      <div class="w-full mt-4 p-3 flex flex-row bg-light-500 rounded-lg text-xl text-black font-semibold hover:bg-light-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500 transition duration-200 cursor-pointer" tabindex="3">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M14.75 15c.966 0 1.75.784 1.75 1.75l-.001.962c.117 2.19-1.511 3.297-4.432 3.297c-2.91 0-4.567-1.09-4.567-3.259v-1c0-.966.784-1.75 1.75-1.75h5.5Zm-11-5h4.376a4.007 4.007 0 0 0 1.067 3.85l.162.151L9.25 14a2.75 2.75 0 0 0-2.649 2.008l-.034.001C3.657 16.009 2 14.919 2 12.75v-1c0-.966.784-1.75 1.75-1.75Zm16.5 0c.966 0 1.75.784 1.75 1.75l-.001.962c.117 2.19-1.511 3.297-4.432 3.297l-.169-.002a2.756 2.756 0 0 0-2.451-2L14.75 14l-.105.001a3.99 3.99 0 0 0 1.229-4L20.25 10ZM12 8a3 3 0 1 1 0 6a3 3 0 0 1 0-6ZM6.5 3a3 3 0 1 1 0 6a3 3 0 0 1 0-6Zm11 0a3 3 0 1 1 0 6a3 3 0 0 1 0-6Z" /></svg>
        <span class="ml-2">Families</span>
      </div>
      <div class="w-full mt-4 p-3 flex flex-row bg-light-500 rounded-lg text-xl text-black font-semibold hover:bg-light-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500 transition duration-200 cursor-pointer" tabindex="4">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M16 3.75a.75.75 0 0 0-.75-.75h-6.5l-.102.007A.75.75 0 0 0 8 3.75V7H6.25A3.25 3.25 0 0 0 3 10.25v6.5A3.25 3.25 0 0 0 6.25 20h11.5A3.25 3.25 0 0 0 21 16.75v-6.5A3.25 3.25 0 0 0 17.75 7H16V3.75Zm-6.5.75h5V7h-5V4.5Zm2 11.25V14H9.75a.75.75 0 0 1 0-1.5h1.75v-1.75a.75.75 0 0 1 1.5 0v1.75h1.75a.75.75 0 0 1 0 1.5H13v1.75a.75.75 0 0 1-1.5 0Z" /></svg>
        <span class="ml-2">Medical</span>
      </div>
      <div class="w-full mt-4 p-3 flex flex-row bg-light-500 rounded-lg text-xl text-black font-semibold hover:bg-light-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500 transition duration-200 cursor-pointer" tabindex="5">
        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M1 8.574V4.428a1.5 1.5 0 0 1 .83-1.342l3.5-1.75a1.5 1.5 0 0 1 1.34 0l3.5 1.75A1.5 1.5 0 0 1 11 4.428v4.146a1.5 1.5 0 0 1-.83 1.341l-3.5 1.75a1.5 1.5 0 0 1-1.34 0l-3.5-1.75A1.5 1.5 0 0 1 1 8.574Zm1.553-4.047a.5.5 0 0 0 .223.67L5.5 6.56V9.5a.5.5 0 1 0 1 0V6.56l2.724-1.362a.5.5 0 1 0-.448-.895L6 5.692L3.224 4.303a.5.5 0 0 0-.671.224Zm9-1.527A2.5 2.5 0 0 1 12 4.428v4.145a2.5 2.5 0 0 1-1.382 2.236l-3.5 1.75a2.5 2.5 0 0 1-2.236 0L2 11.12v6.131a2.25 2.25 0 0 0 2.04 2.24a3 3 0 0 0 5.919.01h2.082a3 3 0 0 0 5.918 0h1.791A2.25 2.25 0 0 0 22 17.25v-5.412a2.25 2.25 0 0 0-.217-.963l-1.699-3.588A2.25 2.25 0 0 0 18.051 6H16.5v-.75A2.25 2.25 0 0 0 14.25 3h-2.697Zm7.697 12.5h1.25V17h-1.25a.75.75 0 1 1 0-1.5Zm-.521-7.57L20.183 11H16.5V7.5h1.55a.75.75 0 0 1 .679.43ZM8.5 19a1.5 1.5 0 1 1-3 0a1.5 1.5 0 0 1 3 0Zm6.5-1.5a1.5 1.5 0 1 1 0 3a1.5 1.5 0 0 1 0-3Z" /></svg>
        <span class="ml-2">Relief</span>
      </div>
    </nav>
    <div class="flex flex-col flex-1 bg-white">
      <header class="h-16 p-5 flex flex-row bg-white drop-shadow-border z-10">
        <svg
          xmlns="http://www.w3.org/2000/svg" class="self-center p-1 rounded bg-light-500 hover:bg-light-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500 transition duration-200 cursor-pointer" tabindex="5"
          width="25" height="25" viewBox="0 0 24 24"
        ><path fill="currentColor" d="M15.891 3.048a3.578 3.578 0 1 1 5.061 5.06L20.06 9L15 3.94l.891-.892ZM13.94 5l-10 9.999a3.106 3.106 0 0 0-.825 1.477L2.02 21.077a.75.75 0 0 0 .904.903l4.601-1.095a3.105 3.105 0 0 0 1.477-.826L19 10.062L13.939 5Z" /></svg>
        <h1 class="ml-3 mt-[-0.3rem] text-2xl font-bold align-text-top">
          Evacuation Center Name
        </h1>
      </header>
      <main class="flex-1 p-5 bg-white drop-shadow-border z-0">
        <section class="grid grid-cols-3 gap-4 border-0 border-dark-500">
          <AnalyticsCard :analytics-data="analyticsData.evacuees" />
          <AnalyticsCard :analytics-data="analyticsData.families" />
          <AnalyticsCard :analytics-data="analyticsData.medical" />
        </section>
      </main>
    </div>
  </div>
</template>

<script>
import AnalyticsCard from '@/components/AnalyticsCard.vue'
import { reactive } from 'vue'

export default {
  components: { AnalyticsCard },
  setup () {
    const analyticsData = reactive({
      evacuees: {
        label: 'Evacuees',
        value: 222,
        img: 'analytics_evacuees.png'
      },
      families: {
        label: 'Families',
        value: 43,
        img: 'analytics_family.png'
      },
      medical: {
        label: 'Needs Medical Assistance',
        value: 14,
        img: 'analytics_aid.png'
      }
    })
    return { analyticsData }
  }
}
</script>

<style lang="scss" scoped>

</style>
