// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var barChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 2000,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});

var buildBar = function (ctx) {
    $.get( ctx.getAttribute('data-uri'), function (data) {
        var counts = Object.values(data);
        var maxVal = Math.max.apply(null, counts);
        barChart.data.labels =  Object.keys(data);
        barChart.data.datasets[0].data = counts;
        barChart.options.scales.yAxes[0].ticks.max = maxVal + maxVal/10;
        barChart.update();
    });
};


$(document).ready(function() {
    buildBar(ctx);
});
