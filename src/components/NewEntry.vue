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

        <div class="p-5 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'evacuee'">
            <h3>New evacuee</h3>
            <button class="mt-auto mx-auto p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
        </div>

        <div class="p-5 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'family'">
            <h3>New family</h3>
            <button class="mt-auto mx-auto p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
        </div>

        <div class="p-5 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'medical'">
            <h3>New medical report</h3>
            <button class="mt-auto mx-auto p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
        </div>

        <div class="p-5 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'relief'">
            <h3>New relief operation</h3>
            <button class="mt-auto mx-auto p-2 btn btn-danger rounded-3 btn-newEntry-close" type="button" @click="openNewEntryForm('')">
                    <h5>Close</h5> </button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'NewEntry',
    data() {
        return {
            newEntryDialogState : 'menu'
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