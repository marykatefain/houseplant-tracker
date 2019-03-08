<template>
  <div class="hello">
    <h1>PLANTS VUE WOO</h1>
    <a @click="fetchPlants">Get the plants</a>
    {{ plants }}
  </div>
</template>

<script>
import client from '../client'
import gql from 'graphql-tag'

export default {
  name: 'Plants',
  data() {
    return {
      plants: []
    }
  },
  created() {
    this.fetchPlants()
  },
  methods: {
    fetchPlants(){
      const query = gql(`
        query{
          plants {
            id
            nickName
          }
        }
      `)

      client.query({ query })
        .then(result => {
          this.plants = result.data.plants
          console.log("RESULT:")
          console.log(result.data.plants)
          console.log("THIS DOT PLANTS:")
          console.log(this.plants)
        })
    },
  },
}
</script>

<style scoped>

</style>
