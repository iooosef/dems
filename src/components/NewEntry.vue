<template>
  <PrimeDialog
    v-model:visible="displayModalProp" modal="true"
    :closable="true" :draggable="false"
    class="w-6/12 [&>*]:!bg-white [&>*:nth-child(2)]:!rounded-t-lg [&>*:nth-child(3)]:!rounded-b-lg"
  >
    <template #header>
      <h2 class="text-2xl font-bold">
        Select a new entry
      </h2>
    </template>
    <div class="mt-2 grid grid-cols-2 grid-rows-2 gap-3">
      <button class="p-4 rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        test
      </button>
      <button class="p-4 rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        test
      </button>
      <button class="p-4 rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        test
      </button>
      <button class="p-4 rounded-lg bg-primary-500 rounded-lg text-xl text-white font-medium hover:bg-primary-700 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50 transition duration-200 cursor-pointer">
        test
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
