<template>
  <!-- hellodfdsfds -->
  <div class="hello">
    <h2>New Plant:</h1>
    <div class="new-plant">
      <div>
        Nickname: {{ newPlantInfo.nickName }}
      </div>
  </div>
</template>

<script>
import client from '../client'
import gql from 'graphql-tag'

export default {
  name: 'NewPlant',
  props: {
    newPlantInfo: {
      type: Object,
      default: {},
    },
  }
  data() {
  },
  created() {
  },
  methods: {

  },
}
</script>

<style scoped>

</style>
