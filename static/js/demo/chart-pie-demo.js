// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var a=document.getElementById("used_car").value;
var b=document.getElementById("used_bike").value;
var c=document.getElementById("used_cgv").value;
var d=document.getElementById("used_cpv").value;

if (a<=0){a=0;}
if (b<=0){b=0;}
if (c<=0){c=0;}
if (d<=0){d=0;}

console.log(a)
console.log(b)
console.log(c)
console.log(d)

var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Car", "Bike", "CGV", "CPV"],
    datasets: [{
      data: [a, b, c, d],
      backgroundColor: ['#c1141e', '#1448ac', '#f6c017', '#6bc242'],
      hoverBackgroundColor: ['#eb010f', '#0b59ef', '#f1b700', '#339f00'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
