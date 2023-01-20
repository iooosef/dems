import { ref, reactive } from 'vue'

export const displayNewEntry = ref(false)
export const displayNewEntryForms = reactive({
  evacuees: false,
  families: false,
  medical: false,
  relief: false
})

export function openEvacueeModal () {
  displayNewEntry.value = false
  displayNewEntryForms.evacuees = true
}
export function closeFormModal () {
  displayNewEntry.value = true
  for (const item in displayNewEntryForms) {
    displayNewEntryForms[item] = false
  }
}
