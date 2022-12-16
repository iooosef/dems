<template>
    <main class="row g-0">
        <aside class="col-md-2 p-3 d-flex flex-column flex-shrink-0 border">
            <div class="nav navbar-brand mb-4 p-2 d-flex justify-content-center">
                <img src="../assets/img/logo.png" class="img-fluid" style="width: 80%;">
            </div>
            <ul class="nav nav-pills d-flex flex-column mb-auto">
                <button class="mb-3 px-2 py-4 d-flex flex-row align-items-stretch btn-success rounded-3 text-light btn btn-newEntry" type="button" @click="btnNewEntryClickedMain">
                    <img src="../assets/img/add.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center"><b>New Entry</b></h5>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('db_evacuees')">
                    <img src="../assets/img/evacuees.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <span class="d-flex align-items-center">Evacuees</span>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('db_families')">
                    <img src="../assets/img/family.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <span class="d-flex align-items-center">Families</span>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('db_medAssist')">
                    <img src="../assets/img/medical.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <span class="d-flex align-items-center">Medical</span>
                </button>
                <button class="p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('db_relief')">
                    <img src="../assets/img/relief.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <span class="d-flex align-items-center">Relief</span>
                </button>
            </ul>
            <ul class="nav nav-pills d-flex flex-column-reverse mt-auto">
                <button class="mt-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/img/help.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <span class="d-flex align-items-center">Help</span>
                </button>
            </ul>
        </aside>
        <div class="h-100 p-0 col-md-10 d-flex flex-column">
            <nav class="px-4 py-2 d-flex flex-row border">
                <button class="me-3 btn btn-light btn-navbar-edit" type="button" @click="btnEvanInfoClicked">
                    <img src="../assets/img/edit.png" class="my-auto img-fluid">
                </button>
                <h4 class="d-flex align-items-center"> {{ this.fetchedEvacInfo }}</h4>
            </nav>
            <section class="d-flex flex-column px-4b pt-4b pb-1">
                <div class="mb-4b d-flex flex-row">
                    <div class="px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Evacuees</b></span>
                            <span class="analytics-number">{{ this.statsEvacInfo[0] }}</span>
                        </div>
                        <img src="../assets/img/analytics_evacuees.png" class="my-auto ms-auto">
                    </div>
                    <div class="mx-5 px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Families</b></span>
                            <span class="analytics-number">{{ this.statsEvacInfo[1] }}</span>
                        </div>
                        <img src="../assets/img/analytics_family.png" class="my-auto ms-auto">
                    </div>
                    <div class="px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Needs Medical Assistance</b></span>
                            <span class="analytics-number">{{ this.statsEvacInfo[2] }}</span>
                        </div>
                        <img src="../assets/img/analytics_aid.png" class="my-auto ms-auto">
                    </div>
                </div>
                <MainTable
                    :fetchedDBevac="fetchedDBevac" 
                    :fetchedDBfamilies="fetchedDBfamilies"
                    :fetchedDBmed="fetchedDBmed"
                    :fetchedDBrelief="fetchedDBrelief"
                    :tableLabel="tableLabel" 
                    :tableActiveHeaders="tableActiveHeaders" />
            </section>
        </div>
    </main>
</template>

<script>
    import MainTable from './MainTable.vue'

    // Expose the `sayHelloJS` function to Python as `say_hello_js`
    function sayHelloJS(x) {
        console.log("Hello from " + x + " using SayHelloJS()");
    }
    // WARN: must use window.eel to keep parse-able eel.expose{...}
    window.eel.expose(sayHelloJS, "say_hello_js");
    // Test calling sayHelloJS, then call the corresponding Python function
    sayHelloJS("Javascript World!");
    window.eel.say_hello_py("Javascript World!");    

    export default {
        name: 'MainDashboard',
        components: {
            MainTable
        },
        data() {
            return {
                isNewEntryClicked : false,
                tableHeaders : {
                    db_evacuees: [
                        {field: 'evacID', header: 'Evacuee ID'},
                        {field: 'fName', header: 'First Name'},
                        {field: 'mi', header: 'M.I.'},
                        {field: 'lName', header: 'Last Name'},
                        {field: 'suffix', header: 'Suffix'},
                        {field: 'cNumber', header: 'Contact Info'},
                        {field: 'famID', header: 'Family ID'}
                    ],
                    db_families: [
                        {field: 'famID', header: 'Family ID'},
                        {field: 'famName', header: 'Family Name'},
                        {field: 'famAddrss', header: 'Family Address'},
                        {field: 'famCID', header: 'Emergency Contact'},
                        {field: 'cNumber', header: 'Emergency Contact Details'},
                        {field: 'famSize', header: 'Family Size'}
                    ],
                    db_medAssist: [
                        {field: 'medreportID', header: 'Report ID'},
                        {field: 'famID', header: 'Family ID'},
                        {field: 'evacueeName', header: 'Evacuee Name'},
                        {field: 'medCause', header: 'Cause'}
                    ],
                    db_relief: [
                        {field: 'famID', header: 'Family ID'},
                        {field: 'reliefName', header: 'Relief Op Name'},
                        {field: 'reliefDate', header: 'Relief Op Date'},
                        {field: 'reliefRepName', header: 'Representative Name'},
                        {field: 'reliefStatus', header: 'Status'}
                    ]
                },
                tableLabel : 'Evacuees Table',
                tableCurrentHeader : 'evacuee',
                editDrpDownOptionsUpdated: []
            }
        },
        props: ['fetchedEvacInfo',"fetchedDBevac","fetchedDBfamilies","fetchedDBmed","fetchedDBrelief","statsEvacInfo"],
        computed: {
            tableActiveHeaders() {
                return this.tableHeaders[this.tableCurrentHeader]
            },

        },
        methods: {
            changeTable(table) {
                this.tableCurrentHeader = table
                this.$emit('change-table')
                this.changeTableTitle(table)
                console.log("this.statsInfo: ", this.statsInfo)
            },
            changeTableTitle(table) {
                table == 'db_evacuees' ? this.tableLabel = 'Evacuees Table'
                    : table == 'db_families' ? this.tableLabel = 'Families Table'
                    : table == 'db_medAssist' ? this.tableLabel = 'Medical Reports Table'
                    : table == 'db_relief' ? this.tableLabel = 'Relief Operations Table'
                    : '' 
            },
            btnNewEntryClickedMain() {
                this.$emit('new-entry')
            },
            btnEvanInfoClicked() {
                this.$emit('evac-info')
            },
            getAllSiblings() {
                alert(this.parentNode)
            }
        },
        mounted: function() {
            this.changeTable('db_evacuees')
        },
        created() {
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    
</style>
