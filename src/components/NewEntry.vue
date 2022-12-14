<template>
    <v-dialog v-model="newEntryModalState" max-width="500px" persistent>
        <div class="p-5 d-flex flex-column rounded-3 new-entry-dialog" v-if="editEvacDialogState && newEntryDialogState == 'menu'">
            <h3>Create a new entry</h3>
            <button class="my-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('evacuee')">
                    <h5>New Evacuee</h5> </button>
            <button class="mb-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('family')">
                    <h5>New Family</h5> </button>
            <button class="mb-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('medical')">
                    <h5>New Medical Report</h5> </button>
            <button class="mb-3 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('relief')">
                    <h5>New Relief Operation</h5> </button>
                    <v-alert dense outlined type="error" class="mb-3" v-if="reliefIsFamTableEmpty"><b>Family Table is Empty!</b> <br/>
                        Register at least one family first.</v-alert>
            <button class="mt-auto mx-auto p-2 btn btn-danger text-light rounded-3 btn-newEntry-close" type="button" @click="newEntryClose">
                    <h5>Close</h5> </button>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'evacuee'">
            <h3>New evacuee</h3>
            <form @submit.prevent="submitFormEvacuee">
                <div class="mb-3 d-flex flex-column">
                    <label for="first-name" class="align-self-start form-label">First Name</label>
                    <input type="text" id="first-name" class="form-control" v-model.trim.lazy="formValuesEvacuee.first_name" required>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="last-name" class="align-self-start form-label">Last Name</label>
                    <input type="text" id="last-name" class="form-control" v-model.trim.lazy="formValuesEvacuee.last_name" required>
                </div>
                <div class="d-flex flex-row">
                    <div class="w-50 mb-3 d-flex flex-column">
                        <label for="middle_initial" class="align-self-start form-label">M.I.</label>
                        <input type="text" id="middle_initial" class="form-control" v-model.lazy="formValuesEvacuee.middle_initial">
                    </div>
                    <div class="w-50 ms-3 mb-3 d-flex flex-column">
                        <label for="suffix" class="align-self-start form-label">Suffix</label>
                        <input type="text" id="suffix" class="form-control" v-model.lazy="formValuesEvacuee.suffix" placeholder="Jr., Sr., II,. etc.">
                    </div>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="contact-number" class="align-self-start form-label">Contact Number</label>
                    <input type="text" id="contact-number" class="form-control" v-model.lazy="formValuesEvacuee.contact_number" onkeypress="return event.charCode >= 48 && event.charCode <= 57" required>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="family-id" class="align-self-start form-label">Family ID</label>
                    <vSelect id="family-id" :options="editDrpDownOptionsUpdate({}, '')"
                         v-model="formValuesEvacuee['famID']" :reduce="(option) => option.value" >
                        <template #search="{attributes, events}">
                            <input
                                class="vs__search"
                                :required="!formValuesEvacuee['famID']"
                                v-bind="attributes"
                                v-on="events"/>
                        </template>
                    </vSelect>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" id="is_family_contact" class="form-check-input" v-model="formValuesEvacuee.is_family_contact">
                    <label for="is_family_contact" class="align-self-start form-label">Make the person an emergency contact of the family?</label>
                </div>
                <!-- <div class="mb-3 form-check">
                    <input type="checkbox" id="is_relief_rep" class="form-check-input" v-model="formValuesEvacuee.is_relief_rep">
                    <label for="is_relief_rep" class="align-self-start form-label">Make the person the relief goods representative of the family?</label>
                </div> -->
                <button class="w-100 p-2 btn btn-success btn-newEntry text-light rounded-3" type="button" @click="openNewEntryForm('family')">
                    <h5>New Family</h5> </button>
                
                <div class="mt-4 p-4 d-flex justify-content-evenly">
                    <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="submit">
                        <h5>Submit</h5> </button>
                    <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="newEntryDialogState = 'menu'">
                        <h5>Close</h5> </button>
                </div>
            </form>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'family'">
            <h3>New family</h3>
            <form @submit.prevent="submitFormFamily">
                <div class="mb-3 d-flex flex-column">
                    <label for="family-name" class="align-self-start form-label">Family Name</label>
                    <input type="text" id="family-name" class="form-control" v-model.trim.lazy="formValuesFamily.family_name" required>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="address" class="align-self-start form-label">Address</label>
                    <input type="text" id="address" class="form-control" v-model.trim.lazy="formValuesFamily.family_address" required>
                </div>
                <div class="mt-4 p-4 d-flex justify-content-evenly">
                    <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="submit">
                        <h5>Submit</h5> </button>
                    <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="openNewEntryForm('')">
                        <h5>Close</h5> </button>
                </div>
            </form>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'medical'">
            <h3>New medical report</h3>
            <form @submit.prevent="submitFormMedical">
                <div class="mb-3 d-flex flex-column">
                    <label for="family-id" class="align-self-start form-label">Family Name & Emergency Contact</label>
                    <vSelect id="family-id" :options="editDrpDownOptionsUpdate({}, 'famID')" 
                        v-model="formValuesMedical['famID']" :reduce="(option) => option.value" >
                        <template #search="{attributes, events}">
                            <input
                                class="vs__search"
                                :required="!formValuesMedical['famID']"
                                v-bind="attributes"
                                v-on="events"
                            />
                        </template>
                    </vSelect>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="evac-id" class="align-self-start form-label">Evacuee Name</label>
                    <vSelect id="evac-id" :options="editDrpDownOptionsUpdate(formValuesMedical, 'evacID')" 
                        v-model="formValuesMedical['evacID']" :reduce="(option) => option.value" >
                        <template #search="{attributes, events}">
                            <input
                                class="vs__search"
                                :required="!formValuesMedical['evacID']"
                                v-bind="attributes"
                                v-on="events"
                            />
                        </template>
                    </vSelect>
                </div>
                <div class="mb-3 d-flex flex-column">
                    <label for="med-report" class="align-self-start form-label">Medical Issue/Report</label>
                    <input type="text" id="med-report" class="form-control" v-model.trim.lazy="formValuesMedical.medical_issue" required>
                </div>
                <div class="mt-auto d-flex justify-content-evenly">
                    <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="submit">
                        <h5>Submit</h5> </button>
                    <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="openNewEntryForm('')">
                        <h5>Close</h5> </button>
                </div>
            </form>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog new-evacuees-dialog" v-if="newEntryDialogState == 'relief'">
            <h3>New relief operation</h3>
            <form @submit.prevent="submitFormRelief">
                <div class="mb-3 d-flex flex-column">
                    <label for="reliefOp-name" class="align-self-start form-label">Relief Operation Name</label>
                    <input type="text" id="reliefOp-name" class="form-control" v-model.trim.lazy="formValuesRelief.relief_op_name" required>
                </div>
                <div class="mt-4 p-4 d-flex justify-content-evenly">
                    <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="submit">
                        <h5>Submit</h5> </button>
                    <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="openNewEntryForm('')">
                        <h5>Close</h5> </button>
                </div>
            </form>
        </div>

        <div class="px-5 py-4 d-flex flex-column rounded-3 new-entry-dialog evacuation-info-dialog" v-if="newEntryEvacInfo">
            <h3>Evacuation Center Information</h3>
            <form @submit.prevent="submitFormEvacCenter">
                <div class="mb-3 d-flex flex-column">
                    <label for="EvacInfo" class="align-self-start form-label">Relief Operation Name</label>
                    <input type="text" id="EvacInfo" class="form-control" v-model.trim.lazy="formValuesEvacInfo" required>
                </div>
                <div class="mt-4 p-4 d-flex justify-content-evenly">
                    <button class="w-25 me-2 p-2 btn btn-success rounded-3 btn-newEntry-close font-size-sm text-light" type="submit">
                        <h5>Submit</h5> </button>
                    <button class="w-25 ms-2 p-2 btn btn-danger rounded-3 btn-newEntry-close font-size-sm text-light" type="button" @click="newEntryClose">
                        <h5>Close</h5> </button>
                </div>
            </form>
        </div>
    </v-dialog>
</template>

<script>
import vSelect from "vue-select"
import 'material-design-icons-iconfont/dist/material-design-icons.css'

export default {
    name: 'NewEntry',
    icons: {
        iconfont: 'md',
    },
    components: {
        vSelect
    },
    data() {
        return {
            newEntryDialogState : 'menu',
            formValuesEvacuee : {
                first_name: "",
                middle_initial: "",
                suffix: "",
                last_name: "",
                contact_number: "",
                famID: "",
                is_family_contact: false
            },
            formValuesFamily : {
                family_name: "",
                family_address: ""
            },
            formValuesMedical : {
                evacID: "",
                famID: "",
                medical_issue: ""
            },
            formValuesRelief : {
                relief_op_name: ""
            },
            formValuesEvacInfo : '',
            form_evacuees_familyId : [],
            newEntryModalState: this.btnNewEntryState,
            tableLabel: '',
            reliefIsFamTableEmpty: false
        }
    },
    props:['newEntryEvacInfo','btnNewEntryState',"fetchedDBfamilies"],
    computed: {
        editEvacDialogState() {
            console.log(this.newEntryEvacInfo)
            console.log(!this.newEntryEvacInfo)
            return this.newEntryEvacInfo ? !this.newEntryEvacInfo : true
        }
    },
    methods: {
        newEntryClose() {
            this.$emit('new-entry-close')
        },
        openNewEntryForm(newEntryTarget) {
            newEntryTarget == 'evacuee' ? (this.newEntryDialogState = 'evacuee', this.tableLabel = 'Evacuees Table')
                : newEntryTarget == 'family' ? this.newEntryDialogState = 'family'
                : newEntryTarget == 'medical' ? (this.newEntryDialogState = 'medical', this.tableLabel = 'Medical Reports Table')
                : newEntryTarget == 'relief' ? (!Object.keys(this.fetchedDBfamilies).length ? 
                    (this.reliefIsFamTableEmpty = true, this.newEntryDialogState = 'menu') : 
                        (this.reliefIsFamTableEmpty = false, this.newEntryDialogState = 'relief'))
                : this.newEntryDialogState = 'menu'
        },
        // isFamilyTableEmpty() {
        //     if(!this.fetchedDBfamilies) {
                
        //     }
        // },
        submitFormEvacuee() {
            console.log('Form Values of Evacuee: ', {...this.formValuesEvacuee});
            window.eel.sqlInsertEvac({...this.formValuesEvacuee});
            this.$parent.fetch_data_fromPy();
            this.newEntryClose();
        },
        submitFormFamily() {
            console.log('Form Values of Family: ', {...this.formValuesFamily});
            window.eel.sqlInsertFam({...this.formValuesFamily});
            this.$parent.fetch_data_fromPy();
            this.newEntryClose();
        },
        submitFormMedical() {
            console.log('Form Values of Medical: ', {...this.formValuesMedical});
            window.eel.sqlInsertMed({...this.formValuesMedical});
            this.$parent.fetch_data_fromPy();
            this.newEntryClose();
        },
        submitFormRelief() {
            console.log('Form Values of Relief: ', {...this.formValuesRelief});
            window.eel.sqlInsertRelief({...this.formValuesRelief});
            this.$parent.fetch_data_fromPy();
            this.newEntryClose();
        },
        submitFormEvacCenter() {
            console.log('Form Values of Evacuation Center: ', this.formValuesEvacInfo);
            this.newEntryClose();
        },
        editDrpDownOptionsUpdate(currentData, currentField) {
            return this.$parent.drpDownOptionsUpdate(currentData, currentField, this.tableLabel)
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
    overflow-y: scroll;
    overflow-x: hidden;
} 
.evacuation-info-dialog {
    height: 75%;
}
.btn-newEntry-close {
    width: 42%;
}

</style>