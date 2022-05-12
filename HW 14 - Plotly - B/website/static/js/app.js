$(document).ready(function() {
    console.log("Page Loaded");
    doWork();

    $("#selDataset").on("change", function() {
        makeDashboard()
    });
});

// global data because the RESPONSE is not changing
var global_data;

function doWork() {
    // Problem 1: Can I read in the data and then print?
    var url = "static/data/samples.json";
    requestAjax(url);
}

function makeDashboard() {
    let id = $("#selDataset").val();

    createMetadata(id);
    createBarChart(id);
    createBubbleChart(id);
    createGaugeChart(id);
}

function requestAjax(url) {
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            console.log(data);
            global_data = data;
            createDropdown();
            makeDashboard();
        },
        error: function(textStatus, errorThrown) {
            console.log("FAILED to get data");
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
}

// function requestD3(url) {
//     d3.json(url).then(function(data) {
//         console.log(data);

//         createDropdown(data);
//         createMetadata(data);
//         createBarChart(data);
//         createBubbleChart(data);
//     });
// }

function createDropdown() {
    var names = global_data.names;
    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        let html = `<option>${name}</option>`;
        $("#selDataset").append(html);
    }
}

function createMetadata(id) {
    $("#sample-metadata").empty();
    let info = global_data.metadata.filter(x => x.id == id)[0];
    console.log(info);
    Object.entries(info).map(function(x) {
        let html = `<h6>${x[0]}: ${x[1]}</h6>`;
        $("#sample-metadata").append(html);
    });
}

function createBarChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        type: 'bar',
        x: sample.sample_values.slice(0, 10).reverse(),
        y: sample.otu_ids.map(x => `OTU ${x}`).slice(0, 10).reverse(),
        text: sample.otu_labels.slice(0, 10).reverse(),
        orientation: 'h'
    }

    var data1 = [trace1];
    var layout = {
        "title": "Bar Chart Placeholder"
    }

    Plotly.newPlot('bar', data1, layout);
}

function createBubbleChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        x: sample.otu_ids,
        y: sample.sample_values,
        text: sample.otu_labels.slice(0, 10).reverse(),
        mode: 'markers',
        marker: {
            size: sample.sample_values,
            color: sample.otu_ids,
            colorscale: "RdBu"
        }
    }

    var data1 = [trace1];
    var layout = {
        "title": "Bubble Chart Placeholder"
    }

    Plotly.newPlot('bubble', data1, layout);
}
function createGaugeChart(id) {
    let info = global_data.metadata.filter(x => x.id == id)[0];
    let avg = global_data["metadata"].map(x => x.wfreq).reduce((a, b) => a + b, 0) / global_data.metadata.length;

    var trace = {
        domain: { x: [0, 1], y: [0, 1] },
        value: info["wfreq"],
        title: { text: "Speed" },
        type: "indicator",
        mode: "gauge+number+delta",
        delta: { reference: avg.toFixed(2) },
        gauge: {
            axis: { range: [null, 10] },
            steps: [
                { range: [0, 1], color: "#FF5733" },
                { range: [1, 2], color: "#FF5E3C" },
                { range: [2, 3], color: "#FF6C4D" },
                { range: [3, 4], color: "#FF7456" },
                { range: [4, 5], color: "#FF8166" },
                { range: [5, 6], color: "#FF8E75" },
                { range: [6, 7], color: "#FE9A83" },
                { range: [7, 8], color: "#FFAE9B" },
                { range: [8, 9], color: "#FFC4B7" },
                { range: [9, 10], color: "#FFEAE5" },
            ],
            threshold: {
                line: { color: "red", width: 4 },
                thickness: 0.75,
                value: 9.5
            }
        }
    };
    var data1 = [trace];

    var layout = {
        title: "Belly Button Wash Frequency"
    };
    Plotly.newPlot('gauge', data1, layout);
}

