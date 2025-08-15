/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */

const mydata = JSON.parse(document.getElementById('conteo_subject').textContent);

const pieConfig = {
  type: 'pie',
  data: {
    datasets: [
      {
        data: [mydata["pack-4"], mydata["consulta"], mydata["clase-presencial"], mydata["clase-unica"], mydata["otros"]],
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: ['#0694a2', '#1c64f2', '#7e3af2', '#b1677a', '#817b7cff'],
        label: 'Dataset 1',
      },
    ],
    labels: ['Pack de 4 clases virtuales', 'Consulta', 'Clase presencial', 'Clase virtual única', "Otros"],
  },
  options: {
    responsive: true,
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
    },
  },
}

// change this to the id of your chart element in HMTL
const pieCtx = document.getElementById('pie')
window.myPie = new Chart(pieCtx, pieConfig)
