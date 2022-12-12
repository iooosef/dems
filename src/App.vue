<template>
  <NewEntry id="new-entry" @new-entry-close="btnNewEntryClosed" v-if="btnNewEntryState" :newEntryEvacInfo="newEntryEvacInfo" />
  <MainApp id="main-app" 
    @new-entry="btnNewEntryClicked" @evac-info="btnEvacInfoChange" @change-table="fetch_data_fromPy" 
    :fetchedEvacInfo="fetchedEvacInfo"  
    :fetchedDBevac="fetchedDBevac" 
    :fetchedDBfamilies="fetchedDBfamilies"
    :fetchedDBmed="fetchedDBmed"
    :fetchedDBrelief="fetchedDBrelief" />
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

      fetchedDBevac: '',
      fetchedDBfamilies: '',
      fetchedDBmed: '',
      fetchedDBrelief: '',

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
    async fetch_data_fromPy() { // receive data from python
        const dataFetched = await window.eel.passDB_toJS()()
        const evacInfo = await window.eel.passEvacInfo_toJS()()      
        this.fetchedDBevac = JSON.parse(dataFetched['db_evacuees'])      
        this.fetchedDBfamilies = JSON.parse(dataFetched['db_families'])      
        this.fetchedDBmed = JSON.parse(dataFetched['db_medAssist'])      
        this.fetchedDBrelief = JSON.parse(dataFetched['db_relief'])
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
    },
    editDrpDownOptionsUpdate(currentData) {
      let editDrpDownOptions = [];
      if(this.tableLabel === 'Evacuees Table') {
          for (const row of this.fetchedDBfamilies) {
              editDrpDownOptions.push(
                  {label: `Family no. ${row.famID} with 
                      ${this.fetchedDBevac.find(({evacID}) => evacID === row.famCID).fName} 
                          ${this.fetchedDBevac.find(({evacID}) => evacID === row.famCID).lName}`,
                          value: row.famID})
          }
      } 
      else if(this.tableLabel === 'Families Table') {
          for (const row of this.fetchedDBevac) {
              if(currentData.famID === row.famID) {
                  editDrpDownOptions.push(
                      {label: `${row.fName} ${row.lName}`,
                          value: row.evacID})
              }
          }
      } 
      return editDrpDownOptions
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
