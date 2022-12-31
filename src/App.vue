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
export default {
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
</style>