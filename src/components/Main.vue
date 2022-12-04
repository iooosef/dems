<template>
    <main class="row no-gutters">
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
                <!-- <button class="p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/img/gear.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <span class="d-flex align-items-center">Settings</span>
                </button> -->
            </ul>
        </aside>
        <div class="p-0 col-md-10 d-flex flex-column">
            <nav class="px-4 py-2 d-flex flex-row border">
                <button class="me-3 btn btn-light btn-navbar-edit" type="button" @click="btnEvanInfoClicked">
                    <img src="../assets/img/edit.png" class="my-auto img-fluid">
                </button>
                <h4 class="d-flex align-items-center">{{fetchedEvacInfo}}</h4>
            </nav>
            <section class="p-4b">
                <div class="mb-4b d-flex flex-row">
                    <div class="px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Evacuees</b></span>
                            <span class="analytics-number">723</span>
                        </div>
                        <img src="../assets/img/analytics_evacuees.png" class="my-auto ms-auto">
                    </div>
                    <div class="mx-5 px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Families</b></span>
                            <span class="analytics-number">131</span>
                        </div>
                        <img src="../assets/img/analytics_family.png" class="my-auto ms-auto">
                    </div>
                    <div class="px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Needs Medical Assistance</b></span>
                            <span class="analytics-number">23</span>
                        </div>
                        <img src="../assets/img/analytics_aid.png" class="my-auto ms-auto">
                    </div>
                </div>
                <div class="mb-3 px-4 py-2 d-flex flex-row rounded-3 bg-light-gray ">
                    <h5>{{ tableLabel }}</h5>
                    <div class="ms-auto input-group search-box">
                        <div class="input-group-prepend">
                            <button class="btn btn-light rounded-start-3b rounded-end-0 btn-search" type="button">
                                <img src="../assets/img/search.png" class="btn-search-icon">
                            </button>
                          </div>
                        <input type="text" class="form-control rounded-end-3b txtbox-search" placeholder="Search" aria-label="Search" aria-describedby="basic-addon2">
                    </div>
                </div>
                <div class="scroll">
                    <table class="table db-table-main">
                        <thead>
                          <tr>
                            <th v-for="header in tableActiveHeaders" :key="header">{{ header }}</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr v-for="(entry, index) in fetchedDB" :key="index">
                            <td v-for="(data, index) in entry" :key="index">{{data}}</td>
                          </tr>
                        </tbody>
                      </table>
                </div>
            </section>
        </div>
    </main>
</template>

<script>
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
        },
        data() {
            return {
                isNewEntryClicked : false,
                tableHeaders : {
                    db_evacuees: ['Evac ID', 'First Name', 'M.I.', 'Last Name', 'Suffix', 'Contact Info', 'Family ID'],
                    db_families: ['Family ID', 'Family Name', 'Family Address', 'Emergency Contact', 'Emergency Contact Details', 'Family Size'],
                    db_medAssist: ['Family ID', 'Evacuee ID', 'First Name', 'Last Name', 'Cause'],
                    db_relief: ['Family ID', 'Relief Op ID', 'Relief Op Date', 'Representative Name', 'Status']
                },
                tableLabel : 'Evacuees Table',
                tableCurrentHeader : 'evacuee'
            }
        },
        props: ['fetchedDB','fetchedEvacInfo'],
        computed: {
            tableActiveHeaders() {
                return this.tableHeaders[this.tableCurrentHeader]
            }
        },
        methods: {
            changeTable(table) {
                this.tableCurrentHeader = table
                this.$emit('change-table', table)
                this.changeTableTitle(table)
                console.log("CLICKED! fetchedDB value: ", this.fetchedDB)
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
            }
        },
        mounted: function() {
            this.changeTable('db_evacuees')
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    
</style>
