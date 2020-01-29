<template>
  <!-- 한개의 최상위 태그 -->
  <div>
    <TodoList category="취뽀"/>
    <TodoList category="SSAFY"/>
    <TodoList category="ETC."/>
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
   components: {
     TodoList
   }
  }
</script>

<style>
  .todo-list {
    display: inline-block;
  }
</style>