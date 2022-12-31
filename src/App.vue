<template>
  <div class="container-fluid">
    <div class="row vh-100">
      <nav class="col-2 p-4">
        <img src="@/assets/img/logo.png" alt="Disaster Evacuees Management System logo" class="logo">
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
          <Icon icon="dems:pencil-fill" height="1.2rem" />
          <h3 class="ms-3">TEST</h3>
        </header>
        <main class="w-100 p-4">
          <h1>Analytics and Table Here...</h1>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae, earum quis architecto dolores officia
            nostrum nobis debitis saepe? Qui ab dolorum minima? Modi quo consequatur dicta ut reiciendis ducimus ea?</p>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import { Icon } from '@iconify/vue'
import "@/assets/icons"

export default {
  components: {
    Icon
  },
  setup() {


    return {}
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/variables.scss";

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
</style>