import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'
Vue.use(Vuex)

export default new Vuex.Store({ // 저장하는 곳
  state: { // 앱의 상태를 나타냄(데이터)
    token: null
  },
  getters: {
    // computed 
    isLoggedIn(state) {
      return state.token ? true : false
    },
    options(state) {
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state) {
      return state.token ? jwtDecode(state.token).user_id : null
    }
  },
  mutations: { // 상태를 변경하는 함수}, 
    setToken(state, token) { // state필수 첫 요소
      state.token = token
    }
  },
  actions: { // methods느낌 
    login(context, token) {
      context.commit('setToken', token)
    },
    logout(context) {
      context.commit('setToken', null)
    }
  },
  modules: {

  }
})