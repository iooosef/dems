<template>
    <div class="flex flex-row h-screen bg-white">
        <nav class="w-60 p-5 bg-white drop-shadow-border z-20">
            <img src="@/assets/img/logo.png" alt="Disaster Evacuees Management System logo" class="w-full" />
            <div class="w-full mt-5 p-3 bg-primary-500 rounded-lg text-2xl text-white font-semibold
                hover:bg-primary-700 focus:shadow-inner
                focus:outline-none focus:ring focus:ring-offset-0 focus:ring-primary-500/50
                transition-all duration-200"
                tabindex="1">
                New Entry
            </div>
            <div class="w-full mt-4 p-3 bg-light-500 rounded-lg text-xl text-black font-semibold
                hover:bg-light-700 focus:shadow-inner
                focus:outline-none focus:ring focus:ring-offset-0 focus:ring-light-500/50
                transition-all duration-200"
                tabindex="2">
                Evacuees
            </div>
        </nav>
        <div class="flex flex-col flex-1 bg-white">
            <header class="h-16 p-5 bg-white drop-shadow-border z-10">header</header>
            <main class="flex-1 p-5 bg-white drop-shadow-border z-0">main</main>
        </div>
    </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

</style>
