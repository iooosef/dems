<template>
    <div class="mt-4 flex-grow-1">
        <div class="p-3 table-header d-flex justify-content-between bg-dems-light rounded-3">
            <h4>{{ tableLabel }}</h4>
            <div class="search-box bg-dems-light shadow-inset">
                test
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: "MainTable",
    setup () {
        const tableLabel = ref("Table Name")

        return {tableLabel}
    }
}
</script>

<style lang="scss" scoped>
.table-header {
    height: 60px;
}

.search-box {
    width: 200px;
}
</style>