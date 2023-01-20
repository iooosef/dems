import { ref } from 'vue'

export default function dialogModalDisplay () {
  const displayNewEntry = ref(false)
  const displayNewEvacuee = ref(false)
  return { displayNewEntry, displayNewEvacuee }
}
