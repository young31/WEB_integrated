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
- v-for는 반드시 id 값과 매핑이 되어야 됨
    - 자료의 값을 설정해서 지정
    - v-bind:key라는 속성이 있어야 함(pk or 지정 id)
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

### binding(bind $ model)
- v-bind: =\> 속성과 연결됨(style, class 등)
- v-model: =\> 해당 태그의 값과 연결됨(input)

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

## computed
- 복잡한 연산을 통해서 표현되어야 하는 값을 computed에 저장해 놓고 꺼내서 사용
- 함수로서 사용하기 보다는 연산의 결과 값을 저장하는 느낌임(caching)
    - 그때 그때 계산하는 것이 아님(시간함수로 비교해보면 차이가 남)
    - methods와 달리 함수형이 아님


## promise([참고]('../day01/03_promise.js'))
- 비동기작업을 처리 할 때 사용하는 객체
- 성공시 =\> .then()구문으로 // 실패시 =\> .catch()구문으로 진행
- 반드시 상태에 따라 풀어주는 작업이 필요함
- 이를 사용함으로 then/catch의 양방향 컨트롤이 가능할 뿐 아니라
- 순차적으로 then을 연결 시킬 수 있어서 효과적으로 처리할 수 있음
```javascript
    axios.get(API_URL) // promise 객체 반환(resolved <=> rejected)
      .then(response => { // promise 객체를 풀어줄 필요가 있음(resolved 이므로 then method <=> catch)
        console.log(response)
        return response.data
      }
      .catch(error) => { // 양방향으로 컨트롤 가능
          console.error(error)
      })
      .then(data => { // 첫 then return 값이 여기로 들어옴
          console.log(2)
      })
```

### Why?
- javascript는 비동기식으로 진행 =\> request처리 중 기다리지 않고 함수진행(data값 아직 못 받은 상태)  
- 이를 해결하고자 함수를 인자로 넘겨서 작업하게 함(callback 함수)
- 그런데 callback이 많아지면 코드가 깊어지면서 혼돈을 야기함

- !! 이를 해결하고자 promise를 사용하게 됨 !!

### 동기적 처리
- 상황에 따라 비동기적 처리가 필요한 순간이 있음
- 이 상황에서 async/await 형식으로 처리할 수 있음


## Storage
- session
    - session이 닫히면 삭제됨 =\> 임시 저장소
- local
    - 브라우저를 껃다 켜도 남아있음
    - 사용자가 사용하는 서버에 저장함

### lcoal storage
- console에 저장되어있는 객체
- 기본문법
    - 꺼내오기: localStorage.getItem(<key>)
    - 삽입: localStorage.setItem(<key>, <content>)
- 객체삽입: 통째로 삽입하면 '객체' 로저장 =\> serializing하여 json타입으로 저장!!
    - JSON.stringify() and JSON.parse() 형식으로 활용
    - script내에 설정하여 놓고 사용함
    - 함수가 실행되지 않으면 적용불가 =\> 해결위한 속성: watch
- watch: 특정 데이터가 바뀔 때 마다 실행하는 함수 정의
    - 함수이름을 보고 있을 변수명으로 설정!!
    - 배열만 봄 =\> object내에서 변화는 잡아내지 못함
        - handler함수로 처리 해 줌
    - handler: watch 설정한 키의 값으로 들어감
        - 원래 함수를 넣고 ++
        - 'deep=true'옵션을 줌 =\> obj의 nested item도 감시 여부


## component
- 독립적인 기능을 하는 독립적 구조(캡슐화)
- 반복되는 역할을 수행하는것을 쉽게 만들어줌
- 이름은 케밥케이스(소문자 + '-')
- Vue.component(tagname, option)으로 등록(전역)
- component별로 파일을 분리하여 사용

### keys
- template: `(backtick으로 작성)
- data: 함수형으로 작성! + 바로 반환해줘야함 (공간을 공유하는 것을 막아줌)
    - [추가자료](https://kr.vuejs.org/v2/guide/components.html#data-%EB%8A%94-%EB%B0%98%EB%93%9C%EC%8B%9C-%ED%95%A8%EC%88%98%EC%97%AC%EC%95%BC%ED%95%A9%EB%8B%88%EB%8B%A4)
    - 일반 오브젝트로 작성하면 component가 하나의 데이터를 공유할 수 있기 때문
- props: component에 data를 전달할 수 있도록 만드는 속성
    - list타입가능
    - obj타입가능 (넘어오는 타입을 지정해줘야함)
        - 타입을 list로 여러 값 가능
        - null값은 어떤 타입을이든 가능
        - obj형태로 required: true 설정가능
        - obj형태로 default: <value> 가능
            - value가 obj/list면 함수형으로 작성(return)
        - validator옵션 가능
            - validator: function(value){
                return value > 20
            }

- methods