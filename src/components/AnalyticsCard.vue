<template>
    <section class="d-flex flex-row justify-content-between analytics-widget">
        <div class="w-100 d-flex bg-dems-secondary shadow-inset rounded-4"
            v-for="table in analyticsData" :key="table">
            <div class="ps-3 py-3 flex-grow-1">
                <h4>{{table.label}}</h4>
                <h1 class="analytics-data-num">{{ table.value }}</h1>
            </div>
            <div class="p-3 flex-shrink-1">
                <img :src="require(`@/assets/img/${table.img}`)" class="analytics-img" alt="">
            </div>
        </div>
    </section>
</template>

<script>
import { ref } from 'vue';

export default {
    name: "AnalyticsCard",
    setup () {
        const analyticsData = ref({
            "evacuees": {
                "label": "Evacuees", 
                "value":  222,
                "img": "analytics_evacuees.png"
            },
            "families": {
                "label": "Families", 
                "value": 43,
                "img": "analytics_family.png"
            },
            "medical": {
                "label": "Needs Medical Assistance", 
                "value": 14,
                "img": "analytics_aid.png"
            }
        })

        return {analyticsData}
    }
}
</script>

<style lang="scss" scoped>
.analytics-widget {
    gap: 16px;
}

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