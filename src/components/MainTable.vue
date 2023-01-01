<template>
    <div class="mt-4 flex-grow-1">
        <div class="p-3 table-header d-flex justify-content-between bg-dems-light rounded-3">
            <h4>{{ tableLabel }}</h4>
            <div class="search-input-group">
                <Icon icon="dems:search" height="1rem" class="search-icon" />
                <input class="h-100 search-box form-control bg-dems-white shadow-inset" />
            </div>
        </div>
    </div>
</template>

<script>
import { Icon } from '@iconify/vue'
import "@/assets/icons"
import { ref } from 'vue';

export default {
    name: "MainTable",
    components: {
        Icon
    },
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

.search-input-group {
    position: relative;
}
.search-input-group > input {
    width: 200px;
    padding-left: 25px;
}

.search-icon {
    position: absolute;
    top: 0;
    bottom: 0;
    left: .5rem;
    margin: auto 0;
}
</style>