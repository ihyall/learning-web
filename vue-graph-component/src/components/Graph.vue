<script setup>
import * as d3 from "d3";
import { onMounted } from "vue";

async function buildGraphSpace() {
    // set the dimensions and margins of the graph
    var margin = { top: 10, right: 30, bottom: 30, left: 40 },
        width = 400 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    svg = d3.select("#graph-svg")
        .style({"border-width": "4px"})

    g_node = svg.append("g")
        .attr("id", "g-node")

    
}


onMounted(() => { buildGraphSpace() })
</script>

<template>
    <div id="graph-space">
        <svg id="graph-svg"></svg>
    </div>
</template>