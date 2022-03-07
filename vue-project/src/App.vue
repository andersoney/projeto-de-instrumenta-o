<template>
  <div id="app">
    <main>
      <div class="chart">
        <TheWelcome
          url="temperature"
          type="temperature"
        />
      </div>
      <div class="chart">
        <TheWelcome url="pressure" type="pressure" />
      </div>
    </main>
  </div>
</template>
<script>
import TheWelcome from "./components/TheWelcome.vue";
export default {
  components: { TheWelcome },
};
</script>
<style>
.chart {
  width: 40%;
  position: relative;
}
</style>

