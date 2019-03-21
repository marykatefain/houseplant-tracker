<template>
  <div id="app">
    <Plants/>
  </div>
</template>

<script>
import Plants from './components/Plants.vue'

export default {
  name: 'app',
  components: {
    Plants
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
