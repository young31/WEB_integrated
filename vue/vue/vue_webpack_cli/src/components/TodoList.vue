<template>
  <div class="todo-list">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo">
    <button v-on:click="addTodo">+</button>
    <ul>
      <li v-for="todo in todos" v-bind:key="todo.id">
        <span>{{ todo.content }}</span>
        <button v-on:click="removeTodo(todo.id)">x</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    'category': {
      type: String,
      required: true,
    }
    // 속성값으로 null을 주면 어떤 타입이든 허용
  },
  data: function() {
    return {
      todos: [],
      newTodo: '',
    }
  },
  methods: {
    addTodo: function() {
      this.todos.push({
        id: new Date().getTime(),
        content: this.newTodo
      })
      this.newTodo = ''
    },
    removeTodo: function(id) {
      this.todos = this.todos.filter((todo) => (todo.id !== id))
    }
  },
}

</script>

<style>
  .todo-list {
    display: inline-block;
  }
</style>