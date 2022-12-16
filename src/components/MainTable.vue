<template>
    <div class="d-flex flex-column flex-grow-1"> 
        <DataTable class="d-flex flex-column flex-fill" :value="databaseData" 
            v-model:filters="filters" filterDisplay="menu"
            autoLayout="true" responsiveLayout="scroll" 
            :paginator="true" :rows="20" >
            
            <template #header>
                <div class="px-4 py-2 d-flex justify-content-between rounded-3 bg-light-gray">
                    <h5> {{ tableLabel }} </h5>
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
    <v-dialog v-model.lazy="editDialog" max-width="500px" persistent>
        <form @submit.prevent="editSubmit">
        <v-card class="p-4">
          <v-card-title class="text-h5 text-wrap text-center">Edit Row</v-card-title>
            <v-card-text>
            <div v-for="(value, field) in currentRowData" class="mb-3" :key="value">
                <b>{{ formLabel(field, value) }} </b>
                
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
            <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="closeDialog">
                <h5>Close</h5> </button>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
        </form>        
    </v-dialog>

    <v-dialog v-model="deleteConfirmDialog" max-width="500px" persistent>
        <v-card class="p-4">
            <v-dialog v-model="displayDeleteError" max-width="500px" persistent>
                <v-alert prominent type="error" style="margin-left: -1rem;" >
                    <v-row align="center">
                        <v-col class="grow">
                            <h5><b>Error!</b> You cannot delete referenced data.</h5>
                            <i>Delete all the data referencing this row, first. </i>
                        </v-col>
                        </v-row>
                        <v-col class="shrink">
                            <v-btn @click="closeDialog">Okay</v-btn>
                        </v-col>
                </v-alert>
            </v-dialog>
            <v-card-title class="text-h5 text-wrap text-center">Are you sure you want to delete the row?</v-card-title>
            <v-card-text>
            <span v-for="(value, field) in currentRowData" :key="value"><b>{{field}}:</b> {{value}}, &nbsp;</span>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="closeDialog">
                    <h5>No</h5> </button>
                <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="deleteSubmit">
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
            displayDeleteError: false
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
            if(this.tableLabel === 'Evacuees Table') {
                window.eel.sqlUpdateEvac({...this.currentRowData})
                return
            } else if(this.tableLabel === 'Families Table' ) {
                window.eel.sqlUpdateFam({...this.currentRowData})
                return
            } else if(this.tableLabel === 'Medical Reports Table' ) {
                window.eel.sqlUpdateMed({...this.currentRowData})
                return
            } else if(this.tableLabel === 'Relief Operations Table' ) {
                window.eel.sqlUpdateRelief({...this.currentRowData})
                return
            }
            this.closeDialog();
        },
        async deleteSubmit () {
            if(this.tableLabel === 'Evacuees Table') {
                this.displayDeleteError = await window.eel.sqlDeleteEvac({...this.currentRowData})()
                if(this.displayDeleteError) {return}
            } else if(this.tableLabel === 'Families Table' ) {
                this.displayDeleteError = await window.eel.sqlDeleteFam({...this.currentRowData})()
                if(this.displayDeleteError) {return}
            } else if(this.tableLabel === 'Medical Reports Table' ) {
                this.displayDeleteError = await window.eel.sqlDeleteMed({...this.currentRowData})()
                if(this.displayDeleteError) {return}
            } else if(this.tableLabel === 'Relief Operations Table' ) {
                this.displayDeleteError = await window.eel.sqlDeleteRelief({...this.currentRowData})()
                if(this.displayDeleteError) {return}
            }
            this.closeDialog();
        },
        closeDialog() {
            this.$parent.$parent.fetch_data_fromPy()
            this.editDialog = false
            this.deleteConfirmDialog = false
            this.displayDeleteError = false
        },
        dynamicCurrentRowData(currentField){
           if(this.tableLabel === 'Families Table' 
                && ['evacID'].includes(currentField)) {
                    !this.fetchedDBevac.find(x => x['evacID'] === this.currentRowData['evacID']) ? '' : 
                    this.currentRowData['cNumber'] = this.fetchedDBevac.find(x => x['evacID'] === this.currentRowData['evacID'])['cNumber']
            } 
        },
        isRequired(currentField){
            if(this.tableLabel === 'Evacuees Table' 
                && ['fName','lName','famID'].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Families Table' 
                && ['famName','famAddrss','evacID'].includes(currentField)) {
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
                    ['evacID'],[''],['famID','cNumber','famSize']][inputType].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Medical Reports Table' 
                && [['medCause'],
                    ['famID','evacID'],[''],['medreportID']][inputType].includes(currentField)) {
                    return true
            } else if(this.tableLabel === 'Relief Operations Table' 
                && [['reliefName'],
                    ['evacID','reliefStatus'],['reliefDate'],['famID']][inputType].includes(currentField)) {
                    return true
            } else {
                return false
            }
        },
        inputDynamicStyle(currentField){
            // console.log(currentField)
            if(['mi','suffix'].includes(currentField)) {
                return "width: 60px" } 
            if(['cNumber'].includes(currentField)) {
                return "width: 136px" } 
            if(['famID'].includes(currentField)) {
                return "width: 380px" }
            if(['evacID','evacID','reliefRep','reliefStatus'].includes(currentField)) {
                return "width: 260px" } 
        },
        editDrpDownOptionsUpdate(currentData, currentField) {
            this.dynamicCurrentRowData(currentField);
            return this.$parent.$parent.drpDownOptionsUpdate(currentData, currentField, this.tableLabel)
        },
        changeCellOutput(currentData, currentField) {
            // let matchedRow = this.fetchedDBevac.find(({evacID}) => evacID === currentData[currentField])
            if(currentField === 'reliefStatus' && currentData[currentField] === 1) {
                return 'received'
            } else if(currentField === 'reliefStatus') { 
                return 'not received'
            } else {
                return currentData[currentField]
            }
        },
        dateFormat(date) {
            const year = date.getFullYear();
            const month = date.getMonth();
            const day = date.getDate();
            return `${year}-${month}-${day}`
        },
        formLabel(currentField, currentValue) {
            return !this.tableActiveHeaders.find(x => x['field'] === currentField) ?
                (this.tableLabel === 'Families Table' ? 'Emergency Contact' + ' : ' + currentValue :
                    this.tableLabel === 'Medical Reports Table' ? 'Evacuee Name' + ' : ' + currentValue :
                    this.tableLabel === 'Relief Operations Table' ? 'Representative' + ' : ' + currentValue : '') : 
                    (
                        this.tableActiveHeaders.find(x => x['field'] === currentField)['field'] === 'famCID' ||
                        this.tableActiveHeaders.find(x => x['field'] === currentField)['field'] === 'evacueeName' ||
                        this.tableActiveHeaders.find(x => x['field'] === currentField)['field'] === 'reliefRepName' ?
                            '' : this.tableActiveHeaders.find(x => x['field'] === currentField)['header'] + ' : ' + currentValue
                    )
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

