/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */

const pieConfig = {
  type: 'pie',
  data: {
    datasets: [
      {
        data: datos,
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: colores,
        label: 'Dataset 1',
      },
    ],
    labels: etiquetas,
  },
  options: {
    responsive: true,
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
      position: "bottom",
      align: "top",
      fullSize: false,
    },
  },
}

// change this to the id of your chart element in HMTL
const pieCtx = document.getElementById('pie')
window.myPie = new Chart(pieCtx, pieConfig)
