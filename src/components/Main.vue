<template>
    <main class="row no-gutters">
        <aside class="col-md-2 p-3 d-flex flex-column flex-shrink-0 border">
            <div class="nav navbar-brand mb-4 p-2 d-flex justify-content-center">
                <img src="../assets/logo.png" class="img-fluid" style="width: 80%;">
            </div>
            <ul class="nav nav-pills d-flex flex-column mb-auto">
                <button class="mb-3 px-2 py-4 d-flex flex-row align-items-stretch btn rounded-3 text-light btn-newEntry" type="button">
                    <img src="../assets/add.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center"><b>New Entry</b></h5>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/evacuees.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Evacuees</h5>
                </button>
                <button class="mb-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/family.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Families</h5>
                </button>
                <button class="p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/medical.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Medical</h5>
                </button>
            </ul>
            <ul class="nav nav-pills d-flex flex-column-reverse mt-auto">
                <button class="mt-3 p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/help.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Help</h5>
                </button>
                <button class="p-2 d-flex flex-row align-items-stretch btn btn-light btn-sidebar rounded-3" type="button">
                    <img src="../assets/gear.png" class="ms-2 me-3 img-fluid sidebar-logo">
                    <h5 class="d-flex align-items-center">Settings</h5>
                </button>
            </ul>
        </aside>
        <div class="p-0 col-md-10 d-flex flex-column">
            <nav class="px-4 py-2 d-flex flex-row border">
                <button class="me-3 btn btn-light btn-navbar-edit" type="button">
                    <img src="../assets/edit.png" class="my-auto img-fluid">
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
                        <img src="../assets/analytics_evacuees.png" class="my-auto ms-auto">
                    </div>
                    <div class="mx-5 px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Families</b></span>
                            <span class="analytics-number">131</span>
                        </div>
                        <img src="../assets/analytics_family.png" class="my-auto ms-auto">
                    </div>
                    <div class="px-4 py-3 d-flex flex-row analytics rounded-3b border">
                        <div class="d-flex justify-content-between flex-column">
                            <span><b>Needs Medical Assistance</b></span>
                            <span class="analytics-number">23</span>
                        </div>
                        <img src="../assets/analytics_aid.png" class="my-auto ms-auto">
                    </div>
                </div>
                <div class="mb-3 px-4 py-2 d-flex flex-row rounded-3 bg-light-gray ">
                    <h5>Evacuees Table</h5>
                    <div class="ms-auto input-group search-box">
                        <div class="input-group-prepend">
                            <button class="btn btn-light rounded-start-3b rounded-end-0 btn-search" type="button">
                                <img src="../assets/search.png" class="btn-search-icon">
                            </button>
                          </div>
                        <input type="text" class="form-control rounded-end-3b txtbox-search" placeholder="Search" aria-label="Search" aria-describedby="basic-addon2">
                    </div>
                </div>
                <div class="scroll">
                    <table class="table db-table-main">
                        <thead>
                          <tr id="db-table-header">
                            <th>Evac ID</th>
                            <th>First Name</th>
                            <th>M.I.</th>
                            <th>Last Name</th>
                            <th>Suffix</th>
                            <th>Contact</th>
                            <th>Family ID</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>000001</td>
                            <td>Primitivo</td>
                            <td>M.</td>
                            <td>Parayaoan</td>
                            <td>Jr.</td>
                            <td>09123456789</td>
                            <td>001</td>
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
        console.log("Hello from " + x);
    }
    // WARN: must use window.eel to keep parse-able eel.expose{...}
    window.eel.expose(sayHelloJS, "say_hello_js");
    // Test calling sayHelloJS, then call the corresponding Python function
    sayHelloJS("Javascript World!");
    window.eel.say_hello_py("Javascript World!");

    export default {
        name: 'HelloWorld',
        props: {
            msg: String
        },
        methods: {
            sayHelloByEEL() {
                window.eel.say_hello_py("哈哈哈哈!")
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    .sidebar-logo {
        height: auto; 
        width: auto; 
        max-width: 45px; 
        max-height: 45px;
    }

    .btn-navbar-edit {
        padding-right: .5rem;
        padding-left: .5rem;
        background-color: inherit;
        border: 0;
    } .btn-navbar-edit img {
        max-width: 18px; 
        max-height: 18px;
    }

    .btn-newEntry {
        background-color: #1ab759;
    } .btn-newEntry:hover {
        background-color: #1C9F51;
        border-color: #DEDEDE;
    } .btn-newEntry:focus {
        box-shadow: 0 0 0 0.3rem #AAF0CE;
    } .btn-newEntry:disabled {
        background-color: #1ab759;
    }

    .btn-sidebar {
        border: 0;
        color: #000000;
    } .btn-sidebar:hover {
        color: #000000;
    } .btn-sidebar:focus {
        color: #000000;
    } .btn-sidebar:not(:disabled):not(.disabled):active {
        color: #000000;
    }

    .analytics {
        width: 100%;
        background-color: #aaf0ce;
        line-height: 1;
        text-align: left
    } .analytics-number {
        font-size: 2.8rem;
    } .analytics > div > span {
        line-height: 1;
    } .analytics > img {
        max-width: 25%;
    } 

    .search-box {
        width: 25%;
    }

    .btn-search {
        height: 100%;
        border: 1px solid #ced4da;
        border-right-style: none;
        background-color: #fdfefe;
        padding: 0.1rem 0.5rem;
    } .btn-search-icon {
        width: 25px;
    }

    .txtbox-search {
        border-left-style: none;
        padding-left: 0.2rem;
        background-color: #fdfefe;
    }

    .scroll {
        height: 55vh;
        overflow-y: scroll;
    } .db-table-main thead tr th{
        border-top-style: none;
        border-right: 0.8px solid #dee2e6;
        border-left: 0.8px solid #dee2e6;
        padding-top: .2rem;
        padding-bottom: .5rem;
        color: #c2c2c2;
        max-width:100%;
        white-space:nowrap;
    } .db-table-main thead tr th:first-child {
        border-left: 0;
    } .db-table-main thead tr th:last-child {
        border-right: 0;
    }

    .btn-sidebar-evacuees:hover {
        background-color: #5a6268;
        border-color: #545b62;
    }
</style>
