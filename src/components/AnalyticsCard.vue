<template>
    <section class="d-flex flex-row justify-content-between">
        <div class="d-flex flex-fill border border-warning rounded-4">
            <div class="p-3 flex-grow-1">
                <h4>Evacuees</h4>
                <h1 class="analytics-data-num">{{ analytics }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img src="@/assets/img/analytics_evacuees.png" class="analytics-img" alt="">
            </div>
        </div>
        <div class="mx-4 d-flex flex-fill border border-warning rounded-4">
            <div class="p-3 flex-grow-1">
                <h4>Evacuees</h4>
                <h1 class="analytics-data-num">{{ analytics }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img src="@/assets/img/analytics_family.png" class="analytics-img" alt="">
            </div>
        </div>
        <div class="d-flex flex-fill border border-warning rounded-4">
            <div class="p-3 flex-grow-1">
                <h4>Evacuees</h4>
                <h1 class="analytics-data-num">{{ analytics }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img src="@/assets/img/analytics_aid.png" class="analytics-img" alt="">
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "AnalyticsCard",
    setup () {
        let analytics = 231;

        return {analytics}
    }
}
</script>

<style lang="scss" scoped>
.analytics-data-num {
    font-size: 2.8rem;
}

.analytics-img {
    width: 80%;
    height: auto;
    float: right;
}
</style>