<template>
  <PrimeDialog
    v-model:visible="displayModalProp" class="w-6/12" modal="true"
  >
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
      Duis aute isrure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
      cupidatat non proident, sunt in culpa squi officia deserunt mollit anim id est laborum.
    </p>
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
