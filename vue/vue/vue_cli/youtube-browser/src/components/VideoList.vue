<template>
  <div>
    <ul class="list-group">
      <VideoListItem v-for="video in videos" :key="video.id.videoId" :video="video" @videoselect="onVideoSelect"/>
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  methods: {
    onVideoSelect: function(video){
      return this.$emit('videoSelect', video)
    }
  },
  props: {
    videos: {
      type: Array
    }
  }
}
</script>

<style>

</style>