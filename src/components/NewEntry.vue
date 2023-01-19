<template>
  <PrimeDialog
    v-model:visible="displayModalProp" modal="true" :closable="false"
    :draggable="false"
    class="w-6/12 [&>*]:!bg-white [&>*:nth-child(2)]:!rounded-t-lg [&>*:nth-child(3)]:!rounded-b-lg"
  >
    test
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
