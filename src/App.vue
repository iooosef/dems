<template>
  <div class="container-fluid">
    <div class="row vh-100">
      <nav class="col-2 border border-primary">
        sidebar
      </nav>
      <div class="col-10 p-0">
        <header class="w-100 border border-primary">
          test
        </header>
        <main class="w-100 border border-primary">
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
header {
  height: 64px;
}

main {
  height: calc(100% - 64px);
}
</style>