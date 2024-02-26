const dropbox = document.getElementById("choose-file");
const button = document.getElementById("draw-graph");

dropbox.addEventListener("change", getFile);
// dropbox.addEventListener("click", getFile);
// button.addEventListener("click", drawGraph);

let json_data

function getFile() {
    // console.log(dropbox);
    const reader = new FileReader();
    reader.onload = function(e) {
        data = e.target.result;
        // console.log(data);
        json_data = JSON.parse(data);
        // console.log(json_data);
        button.style = "display: true;"
    };
    var file = dropbox.files[0];
    reader.readAsText(file);
}

function drawGraph() {
    console.log(json_data);
    text_data = JSON.stringify(json_data);
    const url = "http://127.0.0.1:8000/api/?data=" + text_data;
    let response = fetch(url, {
        method: "post"
    });
    window.location = "http://127.0.0.1:5500/testing_d3/html/graph.html";
}
