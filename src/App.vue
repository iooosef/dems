<template>
  <NewEntry id="new-entry" @new-entry-close="btnNewEntryClosed" v-if="btnNewEntryState" />
  <MainApp id="main-app" @new-entry="btnNewEntryClicked"/>
</template>

<script>
import MainApp from './components/Main.vue'
import NewEntry from './components/NewEntry.vue'

export default {
  name: 'App',
  components: {
    MainApp,
    NewEntry
  },
  data() {
    return {
      btnNewEntryState: false
    }
  },
  methods: {
    btnNewEntryClicked() {
      this.btnNewEntryState = true
    },
    btnNewEntryClosed() {
      this.btnNewEntryState = false
    }
  }
}
</script>

<style>
#new-entry {
  position: absolute;
  z-index: 20;
}

#main-app {
  z-index: 1;
}
</style>
