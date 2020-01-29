<template>
  <div>
    <img v-for="img in imageUrl" :key="img" :src="`${img}`" alt="dogimage">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Test',
  data() {
    return {
      imageUrl: []
    }
  },  
  method: {
    getImage: function(n) {
      const url = `https://dog.ceo/api/breeds/image/random/${N}`
      axios.get(url)
        .then(reponse => {
          for(image of reponse.data.message) {
            this.imageUrl.push(image)
          }
        })
    }
  }
}
</script>

<style>

</style>