var data = {
    labels: ["Masculino", "Feminino"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(0,0,225,1)",
            strokeColor: "rgba(255,192,203,1)",
            highlightFill: "rgba(220,220,220,0.75)",
            highlightStroke: "rgba(220,220,220,1)",
            data: [80,40]
        }
    ]
};


var ctx = document.getElementById("myChart").getContext("2d");

var myBarChart = new Chart(ctx).Bar(data);
