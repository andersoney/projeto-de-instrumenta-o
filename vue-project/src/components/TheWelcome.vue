<script>
import { Line } from "vue-chartjs";
export default {
  name: "LineChart",
  extends: Line,
  data: () => ({
    chartdata: {
      labels: ["1", "2", "3", "4", "5", "6", "7"],
      datasets: [
        {
          label: "Data One",
          backgroundColor: "#f87979",
          data: [40, 39, 10, 40],
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 0,
      },
    },
    number: 0,
  }),
  mounted() {
    this.renderChart(this.chartdata, this.options);
    setInterval(() => {
      let vetor = [];
      this.chartdata.datasets[0].data.push(Math.random() * 90 + 10);
      // this.chartdata.datasets[0].data.push(this.number);
      this.chartdata.labels.push(this.number);
      if (this.chartdata.datasets[0].data.length > 100) {
        this.chartdata.datasets[0].data.splice();
      }
      this.renderChart(this.chartdata, this.options);
      this.number++;
    }, 1000);
  },
};
</script>