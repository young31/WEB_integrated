# Start
- <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>태그를 head에 추가
- body script에 코드를 작성하면 됨

## intro 특이사항
- django에서 쓰던 방식과 비슷함
    - 아래에서 타겟(id)잡고 위에서 {{ }} 형식으로 interpolation  
        ex) app.message or app.$data.message
    
- web에서 <id.dataname> 식으로 접근할 수 있음 \> 반응형 웹(binding)

- 기본적인 구성은 다음과 같으며 키워드는 이미 지정되어 있다.
  
    ```javascript
    const app = new Vue({
      el: '#app',
      data: {
        message: 'hello vue~'
  }
    })
  ```

- name space가 겹치면 warning을 줌

- vue devtools추가하여 도움을 얻어 보자  

- 이런식으로 쉽게 함수와 연동하여 사용할 수 있다.

  ```javascript
  <button v-on:click="plus">plus</button>
  ```


## 디렉티브
- for, if, on-click같은 것들을 v-디렉티브로 사용할 수 있음

- v-<함수>="함수문법" 의 형태로 사용  

  ```javascript
  <li v-for="todo in todos">
    {{ todo }}
  </li>
  ```

- 여러개의 v-시리즈를 달 수 있음
    - 먼저 쓴 것이 지배적
    - if tag 뒤에 else태그를 두면 알아서 for문 커버 (특수 문법같은 느낌)

## 함수
- vue 인스턴스에 함수를 정의할 때는 function키워드를 사용
- vue 인스턴스에 정의된 함수 내에서 'callback함수'를 사용할 때는 애로우 함수사용(=> 형태)
    ```javascript
    getImage: function(category) {
          if (category === 'dog') {
            const API_URL = 'https://dog.ceo/api/breeds/image/random'
            axios.get(API_URL)
              // function으로 사용하면 문제가 생김(this의 문제)
              .then((response) '=>' {
                this.image = response.data.message
              })
          }
    ```
- !! this: vue instance => 모든 콜백함수는 this가 window !!
    
    - 다시말하면 정의하는 순간 함수 공간이 정해지는 것인가? 이 점을 회피 할 수 있는 것이 arrow function?

## created(key)
- 함수형으로 선언

- html을 랜더하면서 동시에 default 실행을 지정해 줌

  ```javascript
  created: function() {
  let target = ''
  const category = Math.random(0, 1)
  if (category < 0.5) {
    target = 'dog'
  } else {
    target = 'cat'
  }
  this.getImage(target)
  }
  ```

## binding(bind $ model)
- v-bind: =\> 속성과 연결됨(style, class 등)
- v-model: =\> 해당 태그의 값과 연결됨(input)
