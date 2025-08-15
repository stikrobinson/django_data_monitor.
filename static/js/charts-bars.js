/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
const mydata = JSON.parse(document.getElementById('conteo_subject').textContent);
const datos = [mydata["pack-4"], mydata["consulta"], mydata["clase-presencial"], mydata["clase-unica"]]
const colores = ['#0694a2', '#1c64f2', '#7e3af2', '#b1677a']
const etiquetas = [["Pack de", "4 clases", "virtuales"], 'Consulta', ["Clase", "presencial"], ["Clase virtual", "única"]]
if(mydata["otros"] !== 0){
  datos.push(mydata["otros"])
  colores.push('#928689ff')
  etiquetas.push("Otros")
}

const barConfig = {
  type: 'bar',
  data: {
    labels: etiquetas,
    datasets: [{
    data: datos,
    backgroundColor: colores,
  }]},
  options: {
    tooltips: {
      callbacks: {
        title: (tooltipItem, data) => {
          let label = data.labels[tooltipItem[0].index];
          if (Array.isArray(label)) label = label.join(' ');
          return label;
        }
      }
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    },
    responsive: true,
    legend: {
      display: false,
    },
  },
}

const barsCtx = document.getElementById('bars')
window.myBar = new Chart(barsCtx, barConfig)
