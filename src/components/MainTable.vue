
<template>
    <div class="scroll">
        <DataTable :value="databaseData" autoLayout="true" responsiveLayout="scroll"
            :paginator="true" :rows="20">
                <div class="px-4 py-2 d-flex justify-content-between rounded-3 bg-light-gray">
                    <h5 @click="logData"> {{ tableLabel }} </h5>
                    <span class="rounded-3b p-input-icon-left txtbox-search">
                        <i class="pi pi-search txtbox-search" />
                        <InputText class="txtbox-search p-inputtext p-component" placeholder="Search" />
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

export default {
    name:"MainTable",
    components: {
        DataTable, Column, InputText
        // , ColumnGroup, Row
    },
    data() {
        return {
            
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
            this.databaseData = [];
            console.log(this.fetchedDB)
            for (const row in this.fetchedDB) {
                console.log("row: ", this.fetchedDB[row])
                this.databaseData.push(
                    {"famID": this.fetchedDB[row][0],
                    "famName": this.fetchedDB[row][1],
                    "famAddrss": this.fetchedDB[row][2],
                    "famCName": this.fetchedDB[row][3],
                    "famCNumber": this.fetchedDB[row][4],
                    "famSize": this.fetchedDB[row][5]
                })
            }
            this.databaseData2 = JSON.stringify(this.databaseData);
            console.log(this.tableActiveHeaders[0]['field']);
            
            console.log(Object.keys(this.databaseData[0])[0] == this.tableActiveHeaders[0]['field']);
            // console.log("database3: ", this.databaseData3)
            // console.log("database: ", this.databaseData)
            // for (const row in this.fetchedDB) {
            //     console.log("row: ", this.fetchedDB[row])
            //     console.log("parsed data of row: ", JSON.parse(this.fetchedDB[row]))

            // }
        }
    }
}
</script>

<style lang="scss" scoped>
template {
    padding: 0;
    border: solid 1px red;;
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

