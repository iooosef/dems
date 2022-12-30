<template>
  <div class="container-fluid">
    <div class="row vh-100">
      <nav class="col-2">
        sidebar
      </nav>
      <div class="col-10 p-0">
        <header class="w-100">
          test
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
  height: 64px;
  box-shadow: var(--box-shadow-dems);
  clip-path: inset(0px 0px -2rem 0px);
}

main {
  height: calc(100% - 64px);
}
</style>