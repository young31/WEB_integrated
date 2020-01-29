const express = require('express')
const router = express.Router()
const axios = require('axios')
const request = require('request')

router.get('/', function(req, res) {
  // const url = 'https://testapi.openbanking.or.kr/oauth/2.0/authorize'
  // const params = {
  //   response_type: code,
  //   client_id: '5gBFqY9IowKc7r4TpdcXXXP5PaCXJ0rzI52S9PFX',
  //   redirect_uri: 'https://shh-mongodb.herokuapp.com/user',
  //   scope: 'transfer',
  //   state: '12341234123412341234123412341234',
  //   auth_type: '0',
  // }
  // axios.get(url, params)
  //   .then((res) => res.json(res))
  res.json(req.params)
})

router.post('/', function(req, res, next) {
  if (req.params) {
    res.json(res.params)
    next()
  }
  if (req, body) {
    res.json(req.body)
  }
})

// router.post('/', function(req, res) {

//   const targeturl = req.body.urls
//   const options = req.body.options

//   function aa() {
//     return axios.post('http://10.3.17.61:8080/v1/account/list', options).then(response => {
//       return response.data
//     })
//   }

//   aa().then(data => {
//     res.json({ data })
//   })
// })




module.exports = router