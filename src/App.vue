<template>
  <NewEntry id="new-entry" @new-entry-close="btnNewEntryClosed" v-if="btnNewEntryState" />
  <MainApp id="main-app" @new-entry="btnNewEntryClicked" :fetchedDB="fetchedDB" @change-table="fetch_data_fromPy" />
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
      btnNewEntryState: false,
      fetchedDB: ''
    }
  },
  props: {

  },
  methods: {
    parentToChildMethod() {
      console.log("parentToChild Called!");
    },
    async fetch_data_fromPy(table) { // receive data from python
        const dataFetched = await window.eel.passDB_toJS()()        
        console.log("just data: ", dataFetched[table])
        this.fetchedDB = dataFetched[table]
    },
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
  z-index: 10;
}

#main-app {
  z-index: 1;
}
</style>
