<template>
  <div class="todo-input">
    <form action="" class="input-group mb-3" @submit.prevent="onSubmit">
      <input v-model="title" type="text" class="form-control" >
      <button class="btn btn-success"  type="submit">plus</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'TodoInput',
  data() {
    return {
      title: ''
    }
  },
  methods: {
    onSubmit() {
      this.$emit('createTodo', this.title)
      this.title = ''
    }
  }
}
</script>

<style>

</style>