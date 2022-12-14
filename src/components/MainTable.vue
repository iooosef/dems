<template>
    <div class="d-flex flex-column flex-grow-1"> 
        <DataTable class="d-flex flex-column flex-fill" :value="databaseData" 
            v-model:filters="filters" filterDisplay="menu"
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
                    </span>
                 </div>
            </template>

            <Column v-for="colheader of tableActiveHeaders" 
                :field="colheader.field" 
                :header="colheader.header" 
                :key="colheader.field"
                sortable>
                <template #body="{ data, field }">
                    {{ changeCellOutput(data, field) }}
                </template>
            </Column> 
            <Column headerStyle="max-width:2rem; padding-left: 0.5rem;" bodyStyle="padding-left: 0.5rem; text-align:center;">
                <template #body="slotProps">
                    <Button icon="pi pi-pencil " 
                        class="p-button-rounded p-button-info p-button-text btn-delete-row" 
                        @click="editModal(slotProps)"/>
                    <Button icon="pi pi-trash " 
                        class="p-button-rounded p-button-danger p-button-text btn-delete-row" 
                        @click="deleteItemConfirm(slotProps)"/>
                </template>
            </Column>  
        </DataTable>
	</div>
    <v-dialog v-model="editDialog" max-width="500px" persistent>
        <form @submit.prevent="editSubmit">
        <v-card class="p-4">
          <v-card-title class="text-h5 text-wrap text-center">Edit Row</v-card-title>
            <v-card-text>
            <div v-for="(value, field) in currentRowData" class="mb-3" :key="value">
                
                <b>{{tableActiveHeaders.find(x => x.field === field).header}}:</b> {{value}} <br>
                <input type="text" class="form-control" style="width: 100%;" 
                    v-model.trim.lazy="currentRowData[field]" :required="isRequired(field)"
                    v-if="displayEditForm(field, 0)">

                <vSelect id="field" v-model.trim.lazy="currentRowData[field]"     
                    :required="!currentRowData[field]"
                    :options="editDrpDownOptionsUpdate(currentRowData, field)" 
                    class="prime-vue-drpdown" :clear-button="false"
                    style="width: 100%;"
                    :reduce="(option) => option.value" 
                    hide-details="auto"
                    v-if="displayEditForm(field, 1)">
                    <template #search="{attributes, events}">
                        <input
                          class="vs__search"
                          :required="!(currentRowData[field] === 1 || currentRowData[field] === 0 || currentRowData[field])"
                          v-bind="attributes"
                          v-on="events"
                        />
                    </template>
                </vSelect>

                <Datepicker v-model.trim.lazy="currentRowData[field]" model-type="yyyy-MM-dd" required
                    menu-class-name="dp-custom-menu"
                    input-class-name="dp-custom-input"
                    :enable-time-picker="false" :clearable="false" 
                    text-input close-on-scroll auto-apply show-now-button
                    now-button-label="Date Today"
                    style="width: 100%;"
                    v-if="displayEditForm(field, 2)" />

                <input type="text" class="form-control" style="width: 100%;" 
                    :value="currentRowData[field]" required disabled
                    v-if="displayEditForm(field, 3)">
            </div>
            </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="submit">
                <h5>Submit</h5> </button>
            <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="editDialog = false">
                <h5>Close</h5> </button>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
        </form>        
    </v-dialog>

    <v-dialog v-model="deleteConfirmDialog" max-width="500px" persistent>
        <v-card class="p-4">
          <v-card-title class="text-h5 text-wrap text-center">Are you sure you want to delete the row?</v-card-title>
          <v-card-text>
            <span v-for="(value, field) in currentRowData" :key="value"><b>{{field}}:</b> {{value}}, &nbsp;</span>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="deleteConfirmDialog = false">
                    <h5>No</h5> </button>
                <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="rowDelete">
                    <h5>Yes</h5> </button>
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
import Datepicker from '@vuepic/vue-datepicker'


export default {
    name:"MainTable",
    components: {
        DataTable, Column, InputText, Button, vSelect, Datepicker
        
    },
    data() {
        return {
            filters: {
                'global': {value: null, matchMode: FilterMatchMode.CONTAINS}
            },
            currentRowData: {},
            showModal: true,
            editDialog: false,
            deleteConfirmDialog: false,
            displayDeleteBtn: true
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
        editModal(currentData) {
            this.currentRowData = currentData.data
            this.editDialog = true
        },
        deleteItemConfirm(currentData) {
            this.currentRowData = currentData.data
            this.deleteConfirmDialog = true
        },
        editSubmit() {
            this.editDialog = false
        },
        rowDelete() {
            this.editDialog = false
        },
        logData() {
            console.log("this.databaseData: ", this.databaseData)
            console.log(this.tableActiveHeaders[0].field)
        },
        msglog(msg){
            console.log(msg); 
        },
        dynamicCurrentRowData(currentField){
           if(this.tableLabel === 'Families Table' 
                && ['famCID'].includes(currentField)) {
                    this.currentRowData['cNumber'] = this.fetchedDBevac.find(x => x['evacID'] === this.currentRowData['famCID'])['cNumber']
            } else if(this.tableLabel === 'Medical Reports Table' 
                && ['evacID'].includes(currentField)) {
                    this.currentRowData['fName'] = this.fetchedDBevac.find(x => x['evacID'] === this.currentRowData['evacID'])['fName']
                    this.currentRowData['lName'] = this.fetchedDBevac.find(x => x['evacID'] === this.currentRowData['evacID'])['lName']
            }
        },
        isRequired(currentField){
            if(this.tableLabel === 'Evacuees Table' 
                && ['fName','lName','famID'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Families Table' 
                && ['famName','famAddrss','famCID'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Medical Reports Table' 
                && ['famID','evacID','medCause'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Relief Operations Table' 
                && ['reliefName','reliefDate','reliefRep','reliefStatus'].includes(currentField)) {
                    return true
            } else {
                return false
            }
        },
        displayEditForm(currentField, inputType) {
            if(this.tableLabel === 'Evacuees Table' 
                && [['fName','mi','lName','suffix','cNumber'],
                    ['famID'],[''],['evacID']][inputType].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Families Table' 
                && [['famName','famAddrss'],
                    ['famCID'],[''],['famID','cNumber','famSize']][inputType].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Medical Reports Table' 
                && [['medCause'],
                    ['famID','evacID'],[''],['medreportID','fName','lName']][inputType].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Relief Operations Table' 
                && [['reliefName'],
                    ['reliefRep','reliefStatus'],['reliefDate'],['famID']][inputType].includes(currentField)) {
                    return true
            } else {
                return false
            }
        },
        inputDynamicStyle(currentField){
            console.log(currentField)
            if(['mi','suffix'].includes(currentField)) {
                return "width: 60px" } 
            if(['cNumber'].includes(currentField)) {
                return "width: 136px" } 
            if(['famID'].includes(currentField)) {
                return "width: 380px" }
            if(['famCID','evacID','reliefRep','reliefStatus'].includes(currentField)) {
                return "width: 260px" } 
        },
        editDrpDownOptionsUpdate(currentData, currentField) {
            this.dynamicCurrentRowData(currentField);
            return this.$parent.$parent.drpDownOptionsUpdate(currentData, currentField, this.tableLabel)
        },
        changeCellOutput(currentData, currentField) {
            let matchedRow = this.fetchedDBevac.find(({evacID}) => evacID === currentData[currentField])
            console.log("currentData: ", currentData, "\ncurrentField: ",currentField)
            if(currentField === 'reliefStatus' && currentData[currentField] === 0) {
                return 'not received'
            } else if(currentField === 'reliefStatus') { 
                return 'received'
            } else if(currentField === 'famCID') {
                return matchedRow.fName + ' ' + matchedRow.lName
            } else if (currentField === 'reliefRep') {
                return matchedRow.fName + ' ' + matchedRow.lName
            } else {
                return currentData[currentField]
            }
        },
        dateFormat(date) {
            const year = date.getFullYear();
            const month = date.getMonth();
            const day = date.getDate();
            return `${year}-${month}-${day}`
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

