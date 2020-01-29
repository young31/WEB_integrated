<template>
  <div>
    <input type="text" @keydown.enter="oninput" placeholder="검색"><span>press enter</span>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    oninput: function(event){
      // eventlistner 발생 / (name, what)
      this.$emit('inputChange', event.target.value)
    }
  }
}
</script> 

<style>

</style>