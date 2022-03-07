<script>
import { Line } from "vue-chartjs";
import axios from "axios";
export default {
  props: ["url", "type"],
  name: "LineChart",
  extends: Line,
  data: () => ({
    backgroundColor: "rgba(209, 230, 245, 0)",
    borderColors: [
      "rgba(56, 163, 236, 1)",
      "rgba(255, 0, 0, 1)",
      "rgba(0, 255, 0, 1)",
    ],
    chartdata: {
      labels: [],
      datasets: [],
    },
    options: {
      scales: {
        // yAxes: [
        //   {
        //     gridLines: {
        //       display: true,
        //     },
        //     ticks: {
        //       min: 0,
        //       max: 1,
        //     },
        //   },
        // ],
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
    this.axiosInstance = axios.create({
      baseURL: "http://localhost:8081/" + this.url,
      timeout: 1000,
    });
    console.log(this.url);
    this.getData();
    setInterval(() => {
      this.getData();
    }, 300);
  },
  methods: {
    async getData() {
      let datasets = [];
      let types = await this.getTypes();
      let dataLabel;
      await Promise.all(
        types.map(async (element, index) => {
          let data = await this.getDataByType(element.type);
          data = data.map((element) => {
            return element.value;
          });
          dataLabel = [...Array(data.length).keys()];
          datasets.push({
            label: this.upercaseFistletter(this.url) + " " + element.type,
            backgroundColor: this.backgroundColor,
            borderColor: this.borderColors[index],
            data: data,
          });
        })
      );
      this.chartdata.datasets = datasets;
      this.chartdata.labels = dataLabel;
      this.renderChart(this.chartdata, this.options);
    },
    async getTypes() {
      const response = await this.axiosInstance.get("/types");
      return response.data;
    },
    async getDataByType(type) {
      const response = await this.axiosInstance.get("/bytype/" + type);
      return response.data;
    },
    upercaseFistletter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
  },
};
</script>