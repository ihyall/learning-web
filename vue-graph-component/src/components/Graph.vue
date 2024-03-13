<script setup>
import * as d3 from "d3";
import { onMounted } from "vue";

let linkCoords = []

function buildGraphSpace() {
    // set the dimensions and margins of the graph
    let margin = { top: 10, right: 30, bottom: 30, left: 40 },
        width = 600 - margin.left - margin.right,
        height = 600 - margin.top - margin.bottom;

    let svg = d3.select("#graph-svg")
        .style("position", "relative")
        .style("height", height)
        .style("width", width)
        .style("border", "dashed red");
        
    let g_links = svg.append("g")
        .attr("id", "g-links");

    let g_nodes = svg.append("g")
        .attr("id", "g-nodes");
}

function addNode(event) {
    let svg = d3.select(event.currentTarget)

    let g_nodes = svg.select("#g-nodes")

    let nodes = g_nodes
        .append("circle")
        .attr("cx", event.offsetX)
        .attr("cy", event.offsetY)
        .attr("r", 20)
        .style("fill", "rgb(0, 200, 0)")
        .on("click", (event) => addLink(event))
        .on("")
}

function linkClickHandler(event) {
    console.log(event.which)
    if (event.which == 1) {
        console.log("lmb")
    } else {
        console.log("ese")
        if (event.which == 3) {
            console.log("rmb")
            deleteLink(event)
        }
    }
}

function addLink(event) {
    
    if (linkCoords.length < 2) {
        linkCoords.push({ cx: d3.select(event.currentTarget).attr('cx'), cy: d3.select(event.currentTarget).attr('cy')})
        console.log(linkCoords)
    }
    
    if (linkCoords.length == 2)
    {
        let select1 = d3.select(`line[x1='${linkCoords[0]['cx']}'][y1='${linkCoords[0]['cy']}'][x2='${linkCoords[1]['cx']}'][y2='${linkCoords[1]['cy']}']`)._groups[0][0]
        let select2 = d3.select(`line[x1='${linkCoords[1]['cx']}'][x2='${linkCoords[0]['cx']}'][y1='${linkCoords[1]['cy']}'][y2='${linkCoords[0]['cy']}']`)._groups[0][0]
        if ((select1 == null) && (select2 == null))
            {
                if (linkCoords[0]['cx'] != linkCoords[1]['cx'] || linkCoords[0]['cy'] != linkCoords[1]['cy'])
                {
                    let g_links = d3.select("#g-links")

                    let link = g_links
                        .append("line")
                        .attr("x1", linkCoords[0]['cx'])
                        .attr("y1", linkCoords[0]['cy'])
                        .attr("x2", linkCoords[1]['cx'])
                        .attr("y2", linkCoords[1]['cy'])
                        .style("stroke", "rgb(0, 255, 0)")
                        .style("stroke-width", "3px")
                        // .style("pointer-events", "none")
                        .on("contextmenu", (event) => linkClickHandler(event))
                }
            }
        linkCoords = []
    }
}

function deleteLink(event) {
    d3.select(event.currentTarget).remove()
}



onMounted(() => { buildGraphSpace() })
</script>

<template>
    <div>
        <p>Doubleclick to create node</p>
        <p>Click on one node, then on another to create link</p>
        <p>Right click on link to delete</p>
    </div>
    <div id="graph-space">
        <svg id="graph-svg" @dblclick="(event) => addNode(event)"></svg>
    </div>
</template>
