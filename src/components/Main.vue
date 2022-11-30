<template>
    <main class="row no-gutters">
        <aside class="col-md-2 p-3 d-flex flex-column flex-shrink-0 border">
            <div class="nav navbar-brand mb-4 p-2 d-flex justify-content-center">
                <img src="../assets/img/logo.png" class="img-fluid" style="width: 80%;">
            </div>
            <ul class="nav nav-pills d-flex flex-column mb-auto">
                <button class="mb-3 px-2 py-4 d-flex flex-row align-items-stretch btn-success rounded-3 text-light btn-newEntry" type="button" @click="btnNewEntryClickedMain">
                    <img src="../assets/img/add.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center"><b>New Entry</b></h5>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('evacuee', 'db_evacuees')">
                    <img src="../assets/img/evacuees.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Evacuees</h5>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('family', 'db_families')">
                    <img src="../assets/img/family.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Families</h5>
                </button>
                <button class="p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button" @click="changeTable('medAssist', 'db_medAssist')">
                    <img src="../assets/img/medical.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Medical</h5>
                </button>
            </ul>
            <ul class="nav nav-pills d-flex flex-column-reverse mt-auto">
                <button class="mt-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/img/help.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Help</h5>
                </button>
                <button class="p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/img/gear.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Settings</h5>
                </button>
            </ul>
        </aside>
        <div class="p-0 col-md-10 d-flex flex-column">
            <nav class="px-4 py-2 d-flex flex-row border">
                <button class="me-3 btn btn-light btn-navbar-edit" type="button">
                    <img src="../assets/img/edit.png" class="my-auto img-fluid">
                </button>
                <h4 class="d-flex align-items-center">Evacuation Center Name</h4>
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
                    <h5>Evacuees Table</h5>
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
                          <!-- <tr v-for="(entry, index) in tableActiveDB" :key="index">
                            <td v-for="cell in entry" :key="cell"> {{ cell }} </td>
                          </tr> -->
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

    async function fetch_data_fromPy() { // receive data from python
        let x = await window.eel.passDB_toJS()()
        console.log("passDB_toJS() receieved value: ", x);
        return x;
    }
    fetch_data_fromPy();

    export default {
        name: 'MainDashboard',
        components: {
        },
        data() {
            return {
                isNewEntryClicked : false,
                tableHeaders : {
                    evacuee: ['Evac ID', 'First Name', 'M.I.', 'Last Name', 'Suffix', 'Contact Info', 'Family ID'],
                    family: ['Family ID', 'Family Name', 'Family Address', 'Emergency Contact', 'Emergency Contact Details', 'Family Size'],
                    medAssist: ['Family ID', 'Evacuee ID', 'First Name', 'Last Name', 'Cause'],
                    relief: ['Relief Op ID', 'Family ID', 'Evacuee ID']
                },
                tableCurrentHeader : 'evacuee',
                tableCurrentDB: 'db_evacuees'
            }
        },
        props: {
            msg: String
        },
        computed: {
            tableActiveHeaders() {
                return this.tableHeaders[this.tableCurrentHeader]
            },
            tableActiveDB() {
                return this.tableDB[this.tableCurrentDB]
            }
        },
        methods: {
            changeTable(table, row) {
                this.tableCurrentHeader = table
                this.tableCurrentDB = row
            },
            btnNewEntryClickedMain() {
                this.$emit('new-entry')
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    
</style>
