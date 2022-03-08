<template>
  <div id="app">
    <main>
      <div class="container-fluid">
        <MostradorTemperatura
          url="pressure"
          type="pressure"
          :min="-511"
          :max="512"
          :alertMin="-450"
          :alertMax="450"
        ></MostradorTemperatura>
        <MostradorTemperatura
          url="temperature"
          type="temperature"
          :min="0"
          :max="1023"
          :alertMin="40"
          :alertMax="950"
        ></MostradorTemperatura>
      </div>
    </main>
  </div>
</template>
<script>
import TheWelcome from "./components/Grafico.vue";
import MostradorTemperatura from "./components/MostradorTemperatura.vue";
export default {
  components: { TheWelcome, MostradorTemperatura },
};
</script>
<style>
</style>

