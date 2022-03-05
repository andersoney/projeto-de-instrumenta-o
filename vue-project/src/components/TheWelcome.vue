<script>
import { Line } from "vue-chartjs";
import axios from "axios";
export default {
  props: ["url", "type"],
  name: "LineChart",
  extends: Line,
  data: () => ({
    chartdata: {
      labels: ["1", "2", "3", "4", "5", "6", "7"],
      datasets: [
        {
          label: "Data One",
          backgroundColor: "rgba(209, 230, 245, 0.01)",
          borderColor: "rgba(56, 163, 236, 1)",
          data: [40, 39, 10, 40],
        },
        {
          label: "Data One",
          backgroundColor: "rgba(209, 230, 245, 0.01)",
          borderColor: "rgba(255, 0, 0, 1)",
          data: [40, 39, 10, 40],
        },
      ],
    },
    options: {
      scales: {
        yAxes: [
          {
            gridLines: {
              display: true,
            },
            ticks: {
              min: 0,
              max: 1,
            },
          },
        ],
      },
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 0,
      },
    },
    number: 0,
  }),
  mounted() {
    this.getData();
    setInterval(() => {
      this.getData();
    }, 1000);
    this.url1 = "http://localhost:8081/temperature";
    this.url2 = "http://localhost:8081/pressure";
  },
  methods: {
    async getData() {
      var thes = this;
      const response1 = await axios.get(this.url1);
      const response2 = await axios.get(this.url2);
      let label = response1.data.map(function (temp) {
        return temp.id;
      });
      let data1 = response1.data.map(function (temp) {
        return temp["temperature"];
      });
      let data2 = response2.data.map(function (temp) {
        return temp["pressure"];
      });
      this.chartdata.datasets[0].data = data1;
      this.chartdata.datasets[1].data = data2;
      this.chartdata.labels = label;
      this.renderChart(this.chartdata, this.options);
    },
  },
};
</script>