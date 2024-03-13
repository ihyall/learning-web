<script setup>
import Graph from './components/Graph.vue';
</script>

<template>
    <main oncontextmenu="return false;">
        <Graph />
    </main>
</template>


<style scoped>
    main {
        user-select: none;
    }
</style>