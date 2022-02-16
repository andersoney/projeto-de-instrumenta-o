<template>
  <div id="app">
    <main>
      <div class="chart">
        <TheWelcome />
      </div>
      <div class="chart">
        <TheWelcome />
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

