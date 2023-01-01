<template>
  <div class="container-fluid">
    <div class="row vh-100">
      <nav class="col-2 p-4">
        <img src="@/assets/img/logo.png" alt="Disaster Evacuees Management System logo" class="logo" @click="reloadPage">
        <div class="w-100 mt-4 px-3 py-4 btn btn-dems-primary btn-new-entry text-start">
          <Icon icon="dems:add-circle-filled" height="2rem" />
          New Entry
        </div>
        <div class="w-100 mt-3 p-3 btn btn-dems-secondary btn-nav text-start">
          <Icon icon="dems:add-person-filled" height="2rem" />
          Evacuees
        </div>
        <div class="w-100 mt-3 p-3 btn btn-dems-light btn-nav text-start">
          <Icon icon="dems:add-people-filled" height="2rem" />
          Families
        </div>
        <div class="w-100 mt-3 p-3 btn btn-dems-light btn-nav text-start">
          <Icon icon="dems:medpack-filled" height="2rem" />
          Medical
        </div>
        <div class="w-100 mt-3 p-3 btn btn-dems-light btn-nav text-start">
          <Icon icon="dems:package-fill" height="2rem" />
          Relief
        </div>
      </nav>
      <div class="col-10 px-0">
        <header class="w-100 p-4 d-flex flex-row align-items-center">
          <div class="p-1 d-flex justify-content-center align-items-center btn btn-dems-light btn-header-edit">
            <Icon icon="dems:pencil-fill" height="1.2rem" />
          </div>
          <h3 class="ms-3">TEST</h3>
        </header>
        <main class="w-100 p-4 d-flex flex-column">
          <AnalyticsCard />
          <MainTable />
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import { Icon } from '@iconify/vue'
import "@/assets/icons"

import AnalyticsCard from "@/components/AnalyticsCard.vue"
import MainTable from "@/components/MainTable.vue"

export default {
  components: {
    Icon,
    AnalyticsCard,
    MainTable
  },
  setup() {


    return {}
  },
  methods: {
    reloadPage() {
      window.location.reload();
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/variables.scss";

main {
  height: calc(100% - #{$header-height});
}

nav {
  box-shadow: $box-shadow-dems;
}

header {
  height: $header-height;
  box-shadow: $box-shadow-dems;
  clip-path: inset(0px 0px -2rem 0px);
}

main {
  height: calc(100% - $header-height);
}

.logo {
  width: 100%;
}

.btn-new-entry {
  font-size: 1.53vw;
}
.btn-nav {
  font-size: 1.2rem;
}

.btn-header-edit {
  width: 38px;
  height: 38px;
}
</style>