<template>
  <!-- hellodfdsfds -->
  <div class="hello">
    <h1>PLANTS VUE WOO</h1>
    <a @click="fetchPlants">Get the plants</a>
    <div v-for="plant in plants">
      <div>
        {{ plant.nickName }}
      </div>
      <!-- <div>
        {{ plant.species.commonName }}
        ( {{ plant.species.scientificName}} )
      </div>
      <div>
        {{ plant.location }}
      </div>
      <div>
        {{ plant.species.lightRequirement }}
      </div> -->
  </div>
  <form>
    <label>Nickname:</label>
    <input type="text" name="nickName">
    <button @click.prevent="addPlant">Submit</button>
  </form>
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
    addPlant(e){
      // e.preventDefault()
      console.log("add plant")
      const plantMutation = gql(`
        mutation PlantMutation($nickName: String!) {
          addPlant(nickName: $nickName) {
            plant{
              id
              nickName
            }
          }
        }
      `)

      client.mutate({mutation: plantMutation, variables: {nickName: "platy"} })
    },
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
