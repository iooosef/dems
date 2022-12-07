
<template>
    <div class="d-flex flex-column flex-grow-1">
        <DataTable class="d-flex flex-column flex-fill" :value="databaseData" 
            v-model:filters="filters" filterDisplay="menu"
            autoLayout="true" responsiveLayout="scroll" 
            :paginator="true" :rows="20" >
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
            <Column v-for="colheader of tableActiveHeaders" 
                :field="colheader.field" 
                :header="colheader.header" 
                :key="colheader.field"
                sortable></Column>
        </DataTable>
	</div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
// import ColumnGroup from 'primevue/columngroup';     //optional for column grouping
// import Row from 'primevue/row';                     //optional for row
import InputText from 'primevue/inputtext';
import {FilterMatchMode} from 'primevue/api';

export default {
    name:"MainTable",
    components: {
        DataTable, Column, InputText
        // , ColumnGroup, Row
    },
    data() {
        return {
            filters: {
                'global': {value: null, matchMode: FilterMatchMode.CONTAINS}
            }
            
        }
    },
    props: ['fetchedDB', 'tableLabel', 'tableActiveHeaders'],
    computed:{
        databaseData() {
            return this.fetchedDB
        }
    },
    created() {
    },
    mounted() {
    },
    methods: {
        logData() {
            console.log(this.fetchedDB)
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
        padding: 0 !important;
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

