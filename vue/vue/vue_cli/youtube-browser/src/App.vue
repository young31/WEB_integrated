<template>
  <div class="container"> 
    youtube
    <!-- step 3 -->
    <VideoDetail :video="selectedVideo"/>
    <SearchBar @inputChange="onInputChange" />
    <VideoList :videos="videos" @videoSelect="onVideoSelect"/>
  </div>
</template>

<script>
import axios from 'axios'
// step 1
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
import VideoDetail from './components/VideoDetail'

const API_KEY = process.env.VUE_APP_API_KEY // 환경변수
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    // step 2
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      videos: [],
      selectedVideo: null
    }
  },
  props: {
    video: {
      type: Object
    }
  },
  methods: {
    onInputChange: function(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
        .then((response) => {
          this.videos = response.data.items
        })
        .catch((error) => {
          console.error(error)
        })
    },
    onVideoSelect: function(video) {
      this.selectedVideo = video
      console.log(video)
    } 
  }

}
</script>

<style scoped>
  input {
    width: 75%;
  }

  div {
    text-align: center;
    margin: 20px;
  }
</style>