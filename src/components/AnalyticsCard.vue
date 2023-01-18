<template>
    <div class="flex flex-row justify-between p-4 bg-secondary-500 rounded-xl">
        <div class="flex flex-col justify-between">
            <h4 class="text-lg leading-5 font-bold">{{ analyticsData.label }}</h4>
            <span class="text-6xl font-normal">{{ analyticsData.value }}</span>
        </div>
        <img :src="require(`@/assets/img/${analyticsData.img}`)" alt="analytics-img" class="h-20 w-20 self-center">
    </div>
</template>

<script>
export default {
  name: 'AnalyticsCard',
  props: {
    analyticsData: {
      type: Object,
      required: true
    }
  },
  setup (props) {
    return { ...props }
  }
}
</script>

<style lang="scss" scoped>

</style>
