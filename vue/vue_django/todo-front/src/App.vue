<template>
  <div id="app">
    <div id="nav">
      <div v-if="!isLoggedin">
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login  </router-link> 
      </div>
      <div v-else>
        <a href="/logout" @click.prevent="logout">Logout</a> 
        <!-- a tag는 새로고침 >> prevent는 redirect를 방지 -->  
      </div>
    </div>
    <div class="container col-6">
      <router-view/> <!-- index의 component를 끌어와서 씀 -->
    </div>
  </div>
    
</template>

<script>
import router from '@/router'

export default {
  name: 'app',
  // data() {
  //   return {
  //     isloggedin: this.$session.has('jwt')
  //   }
  // },
  computed: {
    isLoggedin() {
      return this.$store.getters.isLoggedIn
    }
  },
  methods: {
    logout: function() {
      this.$session.destroy()
      this.$store.dispatch('logout')
      router.push('login')
    },
    // updated: function() {
    //   this.loggedin = this.$session.has('jwt')
    // }
  },
  mounted() { // 최상위 앱 컴포넌트가 실행이 될 때마다
    if(this.$session.has('jwt')) {
      const token = this.$session.get('jwt')
      this.$store.dispatch('login', token)
    }
  },

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
