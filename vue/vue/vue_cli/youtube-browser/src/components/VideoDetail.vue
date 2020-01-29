<template>
  <div v-if="video">
    <div class="details">
      <h4 v-html="video.snippet.title"></h4>
      <iframe :src="videoUrl" frameborder="0"></iframe>
      <p v-html="video.snippet.description"></p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object
    }
  },
  computed: {
    videoUrl: function() {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style scoped>
  .details {
    margin: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
</style>