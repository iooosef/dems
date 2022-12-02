<template>
    <div class="d-flex justify-content-center block-main">
        <div class="p-5 d-flex flex-column rounded-3 new-entry-dialog" v-if="newEntryDialogState == 'menu'">
            <h3>Create a new entry</h3>
            <button class="my-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('evacuee')">
                    <h5>New Evacuee</h5> </button>
            <button class="mb-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('family')">
                    <h5>New Family</h5> </button>
            <button class="mb-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('medical')">
                    <h5>New Medical Report</h5> </button>
            <button class="mb-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('relief')">
                    <h5>New Relief Operation</h5> </button>
            <button class="mt-auto mx-auto p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="newEntryClose">
                    <h5>Close</h5> </button>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'evacuee'">
            <h3>New evacuee</h3>
            <form action="">
                <div class="mb-3 d-flex flex-column">
                    <label for="first-name" class="align-self-start form-label">First Name</label>
                    <input type="text" id="first-name" class="form-control">
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="last-name" class="align-self-start form-label">Last Name</label>
                    <input type="text" id="last-name" class="form-control">
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="contact-number" class="align-self-start form-label">Contact Number</label>
                    <input type="text" id="contact-number" class="form-control" onkeypress="return event.charCode >= 48 && event.charCode <= 57">
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="family-id" class="align-self-start form-label">Family ID</label>
                    <v-select id="family-id" :options="form_evacuees_familyId"></v-select>
                </div>
            </form>
            <div class="mt-auto d-flex justify-content-between">
                <button class="p-2 btn btn-success rounded-3 btn-newEntry-close" type="button" @click="btnSubmitClick">
                    <h5>Submit</h5> </button>
                <button class="p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
            </div>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'family'">
            <h3>New family</h3>
            <form action="">
                <div class="mb-3 d-flex flex-column">
                    <label for="family-name" class="align-self-start form-label">Family Name</label>
                    <input type="text" id="family-name" class="form-control">
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="address" class="align-self-start form-label">Address</label>
                    <input type="text" id="address" class="form-control">
                </div>
            </form>
            <div class="mt-auto d-flex justify-content-between">
                <button class="p-2 btn btn-success rounded-3 btn-newEntry-close" type="button" @click="btnSubmitClick">
                    <h5>Submit</h5> </button>
                <button class="p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
            </div>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'medical'">
            <h3>New medical report</h3>
            <form action="">
                <div class="mb-3 d-flex flex-column">
                    <label for="evac-id" class="align-self-start form-label">Evacuee Name</label>
                    <v-select id="evac-id" :options="form_evacuees_familyId"></v-select>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="family-id" class="align-self-start form-label">Family Name & Emergency Contact</label>
                    <v-select id="family-id" :options="form_evacuees_familyId"></v-select>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="med-report" class="align-self-start form-label">Medical Issue/Report</label>
                    <input type="text" id="med-report" class="form-control">
                </div>
            </form>
            <div class="mt-auto d-flex justify-content-between">
                <button class="p-2 btn btn-success rounded-3 btn-newEntry-close" type="button" @click="btnSubmitClick">
                    <h5>Submit</h5> </button>
                <button class="p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
            </div>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'relief'">
            <h3>New relief operation</h3>
            <form action="">
                <div class="mb-3 d-flex flex-column">
                    <label for="reliefOp-name" class="align-self-start form-label">Relief Operation Name</label>
                    <input type="text" id="reliefOp-name" class="form-control">
                </div>
            </form>
            <div class="mt-auto d-flex justify-content-between">
                <button class="p-2 btn btn-success rounded-3 btn-newEntry-close" type="button" @click="btnSubmitClick">
                    <h5>Submit</h5> </button>
                <button class="p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
            </div>
        </div>
    </div>
</template>

<script>
import vSelect from "vue-select"

export default {
    name: 'NewEntry',
    components: {
        vSelect
    },
    data() {
        return {
            newEntryDialogState : 'menu',
            form_evacuees_familyId : [
                '001 of Joseph Clarence C. Parayaoan',
                '002 of Rose Angel G. Moncatar',
                '003 of Rigel Jonn G. German'
            ]
        }
    },
    methods: {
        newEntryClose() {
            this.$emit('new-entry-close')
        },
        openNewEntryForm(newEntryTarget) {
            newEntryTarget == 'evacuee' ? this.newEntryDialogState = 'evacuee'
                : newEntryTarget == 'family' ? this.newEntryDialogState = 'family'
                : newEntryTarget == 'medical' ? this.newEntryDialogState = 'medical'
                : newEntryTarget == 'relief' ? this.newEntryDialogState = 'relief'
                : this.newEntryDialogState = 'menu'
        },
        btnSubmitClick () {
            console.log('SUBMITTED');
        }
    }
}
</script>

<style>
.block-main {
    height: 100vh;
    width: 100vw;
    padding-top: 5rem;
    padding-bottom: 5rem;
    background-color: rgba(50, 50, 50, 0.36);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
}
.new-entry-dialog {
    width: 500px;
    height: 100%;
    background-color: var(--bs-body-bg);
    text-align: center;
    overflow:hidden;
} 
.btn-newEntry-close {
    width: 42%;
}

</style>