<template>
  <div class="hello">
    <h1>PLANTS VUE WOO</h1>
    <a @click="fetchPlants">Get the plants</a>
    <div v-for="plant in plants">
      <div>
        {{ plant.nickName }}
      </div>
      <div>
        {{ plant.species.commonName }}
        ( {{ plant.species.scientificName}} )
      </div>
      <div>
        {{ plant.location }}
      </div>
      <div>
        {{ plant.species.lightRequirement }}
      </div>
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
            nickName
            species {
              id
              commonName
              scientificName
              lightRequirement
            }
            profilePic
            location
          }
        }
      `)

      client.query({ query, fetchPolicy: 'network-only', })
      //TODO: change cache status on production later? This prevents cache
        .then(result => {
          this.plants = result.data.plants
        })
    },
  },
}
</script>

<style scoped>

</style>
