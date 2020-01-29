<template>
  <div>
    <div class="spinner-border" v-if="loading" role="status">
      <span class="sr-only"></span>
    </div>

    <div class="login-form" v-if="!loading">
      <div class="alert alert-danger" v-if="!this.errors">
        <div v-for="(error, ids) in errors" :key="ids">
          {{ error }}
        </div>
      </div>

      <div class="form-group">
        <label for="id">ID</label>
        <input id="id" type="text" class="form-control" placeholder="type ID" v-model="credentials.username">
      </div>
      <div class="form-group">
        <label for="password">PW</label>
        <input id="password" type="password" class="form-control" placeholder="type PW" v-model="credentials.password">
      </div>
      <button class="btn btn-success" @click="login">Login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: ''
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      if(this.checkform()) {
        this.loading = true
        const SERVER_IP = process.env.VUE_APP_SERVER_IP
        axios.post(SERVER_IP+'/api_token_auth/', this.credentials)
          .then((res) => {
            // 세션 초기화 (사용)
            this.$session.start()
            // vuex store접근
            this.$store.dispatch('login', res.data.token)

            // 응답결과를 세션에 저장
            this.$session.set('jwt', res.data.token) //key값에 value를 저장
            // console.log(res)
            this.loading = false
            // 세션 끝나면 보내줄 곳
            router.push('/')
          }) 
          .catch((err) => {
            console.log(err)
            this.loading = false
          })
      }
    },
    checkform() {
      this.errors = []
      if(!this.credentials.username) { this.errors.push('check ID') } 
      if(this.credentials.password.length < 8) { this.errors.push('pw should be longer than 8') }
      if(this.errors.length === 0) { return true }
    }
  }
}
</script>

<style>

</style>