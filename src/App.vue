<template>
  <div class="container-fluid">
    <div class="row vh-100">
      <nav class="col-2 p-4">
        <img src="@/assets/img/logo.png" alt="Disaster Evacuees Management System logo" class="logo">
      </nav>
      <div class="col-10 px-0">
        <header class="w-100 p-4">
          <h3>TEST</h3>
        </header>
        <main class="w-100">
          main
        </main>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  setup () {
    

    return {}
  }
}
</script>

<style scoped>
nav {
  box-shadow: var(--box-shadow-dems);
}

header {
  height: var(--header-height);
  box-shadow: var(--box-shadow-dems);
  clip-path: inset(0px 0px -2rem 0px);
}

main {
  height: calc(100% - var(--header-height));
}

.logo {
  width: 100%;
}
</style>