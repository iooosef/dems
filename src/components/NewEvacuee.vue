<template>
  <PrimeDialog
    v-model:visible="displayThisModal" :modal="true"
    :closable="false" :draggable="false"
    class="w-fit [&>*]:!bg-white [&>*:nth-child(2)]:!rounded-t-lg [&>*:nth-child(3)]:!rounded-b-lg"
  >
    <template #header>
      <div class="flex-1 flex flex-row justify-between text-black">
        <h2 class="text-2xl font-bold">
          New Evacuee
        </h2>
        <button class="p-1 text-dark-500 rounded-lg hover:bg-light-500 focus:shadow-inner focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500/50 transition duration-200" @click="$parent.displayNewEvacueeModal = false">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 12 12"><path fill="currentColor" d="m1.897 2.054l.073-.084a.75.75 0 0 1 .976-.073l.084.073L6 4.939l2.97-2.97a.75.75 0 1 1 1.06 1.061L7.061 6l2.97 2.97a.75.75 0 0 1 .072.976l-.073.084a.75.75 0 0 1-.976.073l-.084-.073L6 7.061l-2.97 2.97A.75.75 0 1 1 1.97 8.97L4.939 6l-2.97-2.97a.75.75 0 0 1-.072-.976l.073-.084l-.073.084Z" /></svg>
        </button>
      </div>
    </template>
  </PrimeDialog>
</template>

<script>
import { ref } from 'vue'
import PrimeDialog from 'primevue/dialog'
export default {
  name: 'NewEvacueeModal',
  components: {
    PrimeDialog
  },
  props: {
    display: {
      type: Boolean,
      required: true
    }
  },
  setup (props) {
    const displayThisModal = ref(props.display)
    return { displayThisModal }
  },
  watch: {
    display (updateValue) {
      this.displayThisModal = updateValue
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
