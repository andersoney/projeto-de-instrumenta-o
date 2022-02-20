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
    this.getData();
    setInterval(() => {
      this.getData();
    }, 1000);
  },
  methods: {
    async getData() {
      var thes = this;
      const response = await axios.get(this.url);
      let label = response.data.map(function (temp) {
        return temp.id;
      });
      let data = response.data.map(function (temp) {
        return temp[thes.type];
      });
      this.chartdata.datasets[0].data = data;
      this.chartdata.labels = label;
      this.renderChart(this.chartdata, this.options);
    },
  },
};
</script>