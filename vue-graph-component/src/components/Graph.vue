<script setup>
import * as d3 from "d3";
import { onMounted } from "vue";


async function buildGraphSpace() {
    // set the dimensions and margins of the graph
    let margin = { top: 10, right: 30, bottom: 30, left: 40 },
        width = 700 - margin.left - margin.right,
        height = 700 - margin.top - margin.bottom;

    let svg = d3.select("#graph-svg")
        .style("position", "absolute")
        .style("left", "100px")
        .style("top", "100px")
        .style("height", height)
        .style("width", width);

    let g_nodes = svg.append("g")
        .attr("id", "g-nodes")

    let g_links = svg.append("g")
        .attr("id", "g-links");
}

async function addNode(event) {
    let svg = d3.select(event.currentTarget)

    let g_nodes = svg.select("#g-nodes")

    let nodes = g_nodes
        .append("circle")
        .attr("cx", event.offsetX)
        .attr("cy", event.offsetY)
        .attr("r", 20)
        .style("fill", "rgb(0, 200, 0)")
}

onMounted(() => { buildGraphSpace() })
</script>

<template>
    <div id="graph-space">
        <svg id="graph-svg" @dblclick="(event) => addNode(event)"></svg>
    </div>
</template>
