<template>
  <div>
    <li class="list-group-item">
      <img :src="thumbnailUrl" alt="video">
      <div class="mdedia-body" v-html="video.snippet.title" @click="onVideoSelect"></div>
    </li>
    
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object
    }
  },
  methods: {
    onVideoSelect: function() {
      return this.$emit('videoselect', this.video)
    }
  },
  computed: {
    thumbnailUrl: function() {
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style scoped>
  li {
    display: flex;
    cursor: pointer;
  }

  li:hover {
    background-color: #eeeeee;
  }
</style>