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
        .attr("r",10)
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
            .attr("cx", function (d) { return d.x; })
            .attr("cy", function (d) { return d.y; });
    }
    
//    d3.selectAll("circle").on("click", (event) => console.log(d3.select(event.currentTarget).attr('cx'), d3.select(event.currentTarget).attr('cy')));
    d3.selectAll("circle").on("click", (event) => addLink(event))
}

let linkCoords = []

async function addLink(event) {

    if (linkCoords.length < 2) {
        linkCoords.push({ cx: d3.select(event.currentTarget).attr('cx'), cy: d3.select(event.currentTarget).attr('cy')})
    }
    
    if (linkCoords.length == 2)
    {
        let select1 = d3.select(`line[x1='${linkCoords[0]['cx']}'][y1='${linkCoords[0]['cy']}'][x2='${linkCoords[1]['cx']}'][y2='${linkCoords[1]['cy']}']`)._groups[0][0]
        let select2 = d3.select(`line[x1='${linkCoords[1]['cx']}'][x2='${linkCoords[0]['cx']}'][y1='${linkCoords[1]['cy']}'][y2='${linkCoords[0]['cy']}']`)._groups[0][0]
        if ((select1 == null) && (select2 == null))
            {
                if (linkCoords[0]['cx'] != linkCoords[1]['cx'] || linkCoords[0]['cy'] != linkCoords[1]['cy'])
                {
                    let g_links = d3.select("g")
                    let link = g_links
                        .append("line")
                        .attr("x1", linkCoords[0]['cx'])
                        .attr("y1", linkCoords[0]['cy'])
                        .attr("x2", linkCoords[1]['cx'])
                        .attr("y2", linkCoords[1]['cy'])
                        .style("stroke", "rgb(0, 255, 0)")
                }
            }
        linkCoords = []
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