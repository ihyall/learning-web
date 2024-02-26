import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

button.addEventListener("click", drawGraph);

function drawGraph() {
    // Declare the chart dimensions and margins.
    const width = 1000;
    const height = 600;
    const marginTop = 20;
    const marginRight = 20;
    const marginBottom = 30;
    const marginLeft = 40;

    // Declare the x (horizontal position) scale.
    const x = d3.scaleLinear()
        .domain(d3.extent(json_data, d => d.x)).nice()
        .range([marginLeft, width - marginRight]);

    // Declare the y (vertical position) scale.
    const y = d3.scaleLinear()
        .domain(d3.extent(json_data, d => d.y)).nice()
        .range([height - marginBottom, marginTop]);

    // Create the SVG container.
    const svg = d3.create("svg")
        .attr("width", width)
        .attr("height", height);

    // Add the x-axis.
    svg.append("g")
        .attr("transform", `translate(0,${height - marginBottom})`)
        .call(d3.axisBottom(x));

    // Add the y-axis.
    svg.append("g")
        .attr("transform", `translate(${marginLeft},0)`)
        .call(d3.axisLeft(y));
        
    // Add a layer of dots.
    svg.append("g")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("fill", "none")
        .selectAll("circle")
        .data(json_data)
        .join("circle")
            // .attr("cx", json_data["x"].map(q => x(q)))
            .attr("cx", q => x(q.x))
            // .attr("cy", json_data["y"].map(q => y(q)))
            .attr("cy", q => y(q.y))
            .attr("r", 3);

    svg.append("g")
        .attr("font-family", "sans-serif")
        .attr("font-size", 10)
        .selectAll("text")
        .data(json_data)
        .join("text")
        .attr("dy", "0.35em")
        .attr("x", d => x(d.x))
        .attr("y", d => y(d.y) + 7)
        // .style("fill", "white")
        .attr("style", "fill: white")
        .text(d => d.name);

    // Append the SVG element.
    container.append(svg.node());
};
