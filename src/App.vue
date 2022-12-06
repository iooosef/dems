<template>
  <NewEntry id="new-entry" @new-entry-close="btnNewEntryClosed" v-if="btnNewEntryState" :newEntryEvacInfo="newEntryEvacInfo" />
  <MainApp id="main-app" @new-entry="btnNewEntryClicked" @evac-info="btnEvacInfoChange" :fetchedDB="fetchedDB" :fetchedEvacInfo="fetchedEvacInfo" @change-table="fetch_data_fromPy" />
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
      fetchedDB: '',
      fetchedEvacInfo: '',
      newEntryEvacInfo: ''
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
        const evacInfo = await window.eel.passEvacInfo_toJS()()      
        console.log("just data: ", dataFetched[table])
        // for (const row in dataFetched[table]) {
        //   console.log(dataFetched[table][row])
        //   console.log("parsed data: ", JSON.parse(dataFetched[table][row]))
        // }
        this.fetchedDB = JSON.parse(dataFetched[table])
        this.fetchedEvacInfo = evacInfo
    },
    btnNewEntryClicked() {
      this.btnNewEntryState = true
      this.newEntryEvacInfo = false
    },
    btnNewEntryClosed() {
      this.btnNewEntryState = false
      this.newEntryEvacInfo = false
    },
    btnEvacInfoChange() {
      this.btnNewEntryState = true
      this.newEntryEvacInfo = true
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
