<template>
    <div class="d-flex flex-column flex-grow-1">
        
        <DataTable class="d-flex flex-column flex-fill" :value="databaseData" 
            v-model:filters="filters" filterDisplay="menu"
            editMode="row" v-model:editingRows="editingRows" @row-edit-save="onRowEditSave"
            autoLayout="true" responsiveLayout="scroll" 
            :paginator="true" :rows="20" >
            
            <template #header>
                <div class="px-4 py-2 d-flex justify-content-between rounded-3 bg-light-gray">
                    <h5 @click="logData"> {{ tableLabel }} </h5>
                    <span class="rounded-3b p-input-icon-left txtbox-search">
                        <i class="pi pi-search txtbox-search" />
                        <InputText class="txtbox-search p-inputtext p-component"
                            v-model="filters['global'].value" 
                            placeholder="Search" />
                        <!-- <InputText v-model="filters['global'].value" placeholder="Keyword Search" /> -->
                    </span>
                 </div>
            </template>

            <Column v-for="colheader of tableActiveHeaders" 
                :field="colheader.field" 
                :header="colheader.header" 
                :key="colheader.field"
                sortable>
                <template #body="{ data, field }">
                    <!-- {{data[field]}} -->
                    {{ changeCellOutput(data, field) }}
                </template>
                <template #editor="{ data, field }">
                    {{data[field]}}
                    <InputText v-model="data[field]" 
                        :style="inputDynamicStyle(colheader.field)"
                        v-if="!rowEditTxtBox(colheader.field)"/>

                    <v-select id="field" v-model="data[field]" 
                        class="prime-vue-drpdown"
                        :style="inputDynamicStyle(colheader.field)"
                        :options="editDrpDownOptionsUpdate(data)"     
                        :reduce="(option) => option.value"
                        v-if="rowEditDrpDown(colheader.field)">
                    </v-select>
                </template>
            </Column> 
            <Column :rowEditor="true" headerStyle="max-width:2rem; padding-right: 0.5rem;" bodyStyle="text-align:center; padding-right: 0.5rem;">
            </Column>  
            <Column headerStyle="max-width:2rem; padding-left: 0.5rem;" bodyStyle="padding-left: 0.5rem; text-align:center;">
                <template #body="slotProps">
                    <Button icon="pi pi-trash " 
                        class="p-button-rounded p-button-danger p-button-text btn-delete-row" 
                        @click="deleteItemConfirm(slotProps)"/>
                </template>
            </Column>  
        </DataTable>
	</div>
    <v-dialog v-model="deleteConfirmDialog" max-width="500px" persistent>
        <v-card class="p-2">
          <v-card-title class="text-h5 text-wrap text-center">Are you sure you want to delete the row?</v-card-title>
          <v-card-text>
            <span v-for="(value, field) in currentRowData" :key="value"><b>{{field}}:</b> {{value}}, &nbsp;</span>
            </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="deleteConfirmDialog = false">No</v-btn>
            <v-btn color="blue darken-1" text @click="msglog()">Yes</v-btn> 
            <!-- //call delete data function -->
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import {FilterMatchMode} from 'primevue/api';
import vSelect from "vue-select";


export default {
    name:"MainTable",
    components: {
        DataTable, Column, InputText, Button, vSelect
    },
    data() {
        return {
            filters: {
                'global': {value: null, matchMode: FilterMatchMode.CONTAINS}
            },
            editDrpDownOptions: [],
            editingRows: [],
            currentRowData: {},
            showModal: true,
            deleteConfirmDialog: false,
        }
    },
    props: ["fetchedDBevac","fetchedDBfamilies","fetchedDBmed","fetchedDBrelief",
        'tableLabel', 'tableActiveHeaders'],
    computed:{
        databaseData() {
                return this.tableLabel === 'Evacuees Table' ? this.fetchedDBevac
                    : this.tableLabel === 'Families Table' ? this.fetchedDBfamilies
                    : this.tableLabel === 'Medical Reports Table' ? this.fetchedDBmed
                    : this.tableLabel === 'Relief Operations Table' ? this.fetchedDBrelief
                    : this.fetchedDBevac  
        }
    },
    methods: {
        deleteItemConfirm(currentData) {
            console.log('currentData: ', currentData.data)
            this.currentRowData = currentData.data
            console.log('currentRowData: ', this.currentRowData)
            this.deleteConfirmDialog = true
        },
        logData() {
            console.log("this.databaseData: ", this.databaseData)
            console.log(this.tableActiveHeaders[0].field)
        },
        msglog(msg){
            console.log(msg); 
        },
        onRowEditSave(event) {
            let { newData, index } = event;
            console.log(newData);
            this.databaseData[index] = newData;
        },
        rowEditTxtBox(currentField) {
            if(this.tableLabel === 'Evacuees Table' 
                && ['evacID','famID'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Families Table' 
                && ['famID','famCName','cNumber','famSize'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Medical Reports Table' 
                && ['famID','evacID','fName','lName'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Relief Operations Table' 
                && !['reliefName'].includes(currentField)) {
                    return true
            } else {
                return false
            }
        },
        rowEditDrpDown(currentField) {
            if(this.tableLabel === 'Evacuees Table' 
                && ['famID'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Families Table' 
                && ['famCName'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Relief Operations Table' 
                && ['reliefRep '].includes(currentField)) {
                    return true
            } else {
                return false
            }
        },
        inputDynamicStyle(currentField){
            if(['mi','suffix'].includes(currentField)){
                return "width: 60px"
            } 
            if(['cNumber'].includes(currentField)) {
                return "width: 136px"
            } 
            if(this.tableLabel === 'Evacuees Table' 
                && ['famID'].includes(currentField)) {
                return "width: 360px"
            }
            if(['famCName'].includes(currentField)) {
                return "width: 250px"
            } 
        },
        editDrpDownOptionsUpdate(currentData) {
            let editDrpDownOptions = [];
            if(this.tableLabel === 'Evacuees Table') {
                for (const row of this.fetchedDBfamilies) {
                    editDrpDownOptions.push(
                        {label: `Family no. ${row.famID} with 
                            ${this.fetchedDBevac.find(({evacID}) => evacID === row.famCName).fName} 
                                ${this.fetchedDBevac.find(({evacID}) => evacID === row.famCName).lName}`,
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
        },
        changeCellOutput(currentData, currentField) {
            if(currentField === 'reliefStatus' && currentData[currentField] === 0) {
                return 'did not received'
            } else if(currentField === 'reliefStatus') { 
                return 'received'
            } else if(currentField === 'famCName') {
                let matchedRow = this.fetchedDBevac.find(({evacID}) => evacID === currentData[currentField])
                return matchedRow.fName + ' ' + matchedRow.lName
            }
            return currentData[currentField]
        }
    }
}
</script>

<style lang="scss" scoped>
template {
    padding: 0;
}

::v-deep(.p-paginator) {
    .p-paginator-current {
        margin-left: auto;
    }
}

::v-deep(.p-progressbar) {
    height: .5rem;
    background-color: #D8DADC;

    .p-progressbar-value {
        background-color: #607D8B;
    }
}

::v-deep(.p-datepicker) {
    min-width: 25rem;

    td {
        font-weight: 400;
    }
}

::v-deep(.p-datatable.p-datatable-customers) {
    .p-datatable-header {
        text-align: left;
        font-size: 1.5rem;
    }

    .p-paginator {
        padding: 0;
    }

    .p-datatable-thead > tr > th {
        text-align: left;
    }

    .p-datatable-tbody > tr > td {
        cursor: auto;
    }

    .p-dropdown-label:not(.p-placeholder) {
        text-transform: uppercase;
    }
}
</style>

