$(document).ready(function() {
    console.log("Page Loaded");
    doWork();
});

function doWork() {
    // Problem 1: Can I read in the data and then print?
    var url = "static/data/samples.json";
    requestAjax(url);
}

function requestAjax(url) {
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            console.log(data);
            createDropdown(data);
            createMetadata(data);
            createBarChart(data);
            createBubbleChart(data);
            createGaugeChart(data);
        },
        error: function(textStatus, errorThrown) {
            console.log("FAILED to get data");
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
}

function requestD3(url) {
    d3.json(url).then(function(data) {
        console.log(data);

        createDropdown(data);
        createMetadata(data);
        createBarChart(data);
        createBubbleChart(data);
        createGaugeChart(data);
    });
}

function createDropdown(data) {
    var names = data.names;
    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        let html = `<option>${name}</option>`;
        $("#selDataset").append(html);
    }
}

function createMetadata(data) {
    let id = $("#selDataset").val();
    let info = data.metadata.filter(x => x.id == id)[0];
    console.log(info);
    Object.entries(info).map(function(x) {
        let html = `<h6>${x[0]}: ${x[1]}</h6>`;
        $("#sample-metadata").append(html);
    });
}

function createBarChart(data) {
    let id = $("#selDataset").val();
    let sample = data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        type: 'bar',
        x: sample.sample_values.slice(0, 10).reverse(),
        y: sample.otu_ids.map(x => `OTU ${x}`).slice(0, 10).reverse(),
        text: sample.otu_labels.slice(0, 10).reverse(),
        orientation: 'h',
        mode: 'markers',
        marker: {
            color: sample.otu_ids
        }

    }

    var data1 = [trace1];
    var layout = {
        "title": "10 OTUs Found",
        xaxis: { title: "Sample Value"},
		yaxis: { title: "OTU ID"}
    }

    Plotly.newPlot('bar', data1, layout);
}

function createBubbleChart(data) {
    let id = $("#selDataset").val();
    let sample = data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        x: sample.otu_ids,
        y: sample.sample_values,
        text: sample.otu_labels.slice(0, 10).reverse(),
        mode: 'markers',
        marker: {
            size: sample.sample_values,
            color: sample.otu_ids
        }
    }

    var data1 = [trace1];
    var layout = {
        "title": "OTU IDs and Value Samples",
        xaxis: { title: "OTU ID"},
		yaxis: { title: "Sample Value"}
    }

    Plotly.newPlot('bubble', data1, layout);
}

function createGaugeChart(num) {
    
    var data1 = [
    {
        domain: { x: [0, 1], y: [0, 1] },
        value: num,
        title: {text: "Belly Button Washing Frequency"},
        type: "indicator",
        mode: "gauge+number+delta",
        gauge: {
            axis: { range: [null, 9]},
            bar: { color: "#000000" },
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
        }
    }];
    Plotly.newPlot('gauge', data1,);
}

