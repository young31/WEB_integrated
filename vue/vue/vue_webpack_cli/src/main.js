import Vue from 'vue' // export default랑 세트
import App from './App.vue'

new Vue({
    render: (h) => h(App) // 최상위 component지정
  }).$mount('#app') // 어디에 작업 (#app인 태그에)