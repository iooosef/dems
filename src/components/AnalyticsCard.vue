<template>
    <section class="d-flex flex-row justify-content-between">
        <div class="w-100 d-flex bg-dems-secondary shadow-inset rounded-4">
            <div class="ps-3 py-3 flex-grow-1">
                <h4>Evacuees</h4>
                <h1 class="analytics-data-num">{{ analytics }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img src="@/assets/img/analytics_evacuees.png" class="analytics-img" alt="">
            </div>
        </div>
        <div class="w-100 mx-4 d-flex bg-dems-secondary shadow-inset rounded-4">
            <div class="ps-3 py-3 flex-grow-1">
                <h4>Families</h4>
                <h1 class="analytics-data-num">{{ analytics }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img src="@/assets/img/analytics_family.png" class="analytics-img" alt="">
            </div>
        </div>
        <div class="w-100 d-flex bg-dems-secondary shadow-inset rounded-4">
            <div class="ps-3 py-3 flex-grow-1">
                <h4>Needs Medical Assistance</h4>
                <h1 class="analytics-data-num">{{ analytics }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img src="@/assets/img/analytics_aid.png" class="analytics-img" alt="">
            </div>
        </div>
    </section>
</template>

<script>
import { ref } from 'vue';

export default {
    name: "AnalyticsCard",
    setup () {
        const analytics = ref(35)

        return {analytics}
    }
}
</script>

<style lang="scss" scoped>
.analytics-data-num {
    font-size: 2.8rem;
    @at-root h4{
        height: 28.8px; 
        white-space: nowrap;
    }
}

.analytics-img {
    width: 96px;
    height: auto;
    float: right;
    @at-root .analytics-img{
        @at-root {
            div:nth-child(2) {width: 112px;}
        }
    }
}
</style>