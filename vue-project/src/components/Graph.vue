<script setup>
import * as d3 from 'd3'
import { onMounted } from 'vue';
import data_network from '../assets/data_network.json'


async function drawGraph() {
    let data = data_network
    console.log("data:", data)

    // set the dimensions and margins of the graph
    var margin = { top: 10, right: 30, bottom: 30, left: 40 },
        width = 400 - margin.left - margin.right,
        height = 400 - margin.top - margin.bottom;

    var svg = d3.select("#svg1")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")")
    // .append("svg")
    // .append("g")


    // initialize the links
    let link = svg
        .selectAll("line")
        .data(data.links)
        .enter()
        .append("line")
        .style("stroke", "rgb(255, 0, 0)")

    // initialize the nodes
    let node = svg
        .selectAll("circle")
        .data(data.nodes)
        .enter()
        .append("circle")
        .attr("r", 20)
        .style("fill", "rgb(0, 200, 0)")

    // Defining force
    let simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink()                               // This force provides links between nodes
            .id(function (d) { return d.id; })                     // This provide  the id of a node
            .links(data.links)                                    // and this the list of links
        )
        .force("charge", d3.forceManyBody().strength(-400))         // This adds repulsion between nodes. Play with the -400 for the repulsion strength
        .force("center", d3.forceCenter(width / 2, height / 2))     // This force attracts nodes to the center of the svg area
        .on("end", ticked);

    function ticked() {
        link
            .attr("x1", function (d) { return d.source.x; })
            .attr("y1", function (d) { return d.source.y; })
            .attr("x2", function (d) { return d.target.x; })
            .attr("y2", function (d) { return d.target.y; });

        node
            .attr("cx", function (d) { return d.x + 6; })
            .attr("cy", function (d) { return d.y - 6; });
    }
}

onMounted(() => { drawGraph() })

</script>


<template>
    <div id="graph1">
        <h2>d3.js graph graph component on Vue.js</h2>
        <svg id="svg1"></svg>
    </div>
</template>