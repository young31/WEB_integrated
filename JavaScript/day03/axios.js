const axios = require('axios')
const url = 'https://jsonplaceholder.typicode.com/posts'

axios.get(url)
  .then(function(response) {
    console.log(response.data)
  })