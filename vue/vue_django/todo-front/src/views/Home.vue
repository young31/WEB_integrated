<template>
  <div class="home">
    <h1>TODO</h1>
    <TodoInput @createTodo="createTodo" />
    <TodoList v-bind:todos="todos" />
  </div>
</template>

<script>
import axios from 'axios'
// import jwtDecode from 'jwt-decode'

import { mapGetters } from 'vuex'

import router from '@/router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'

export default {
  name: 'Home',
  data(){
    return {
      todos: []
    }
  },
  components: {
    TodoList,
    TodoInput
  },
  computed: {
    ...mapGetters( // spreadoperator: 가지고 있는거 다 뿌려
      [
        'isLoggedIn',
        'options',
        'userId'
      ]
    )
  },
  methods: {
    checkLogin() {
      if(!this.isLoggedIn) {// bool값으로 반환
        router.push('/login')
    }
  },
  getTodo() {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    axios.get(SERVER_IP + `/api/v1/users/${this.userId}/`, this.options)
      .then((res) => {
        this.todos = res.data.todo_set
      })
      .catch((err) => {
        console.log('###########', err)
      })
  },
  createTodo(title) {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP

    const data = {
      title,
      user: this.userId
    }

    axios.post(SERVER_IP + `/api/v1/todos/`, data, this.options)
      .then((res) => {
        this.todos.push(res.data)
      })
      // .catch((err) => {
      //   console.log(err)
      // })

  }
},
mounted() {
  if(this.isLoggedIn){
    this.checkLogin()
    this.getTodo()
  }
},
watch: {
  isLoggedIn() {
    this.getTodo()
  }
}
}
</script>

<style>

</style>