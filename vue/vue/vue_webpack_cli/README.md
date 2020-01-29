# project build
## library 준비
1. npm init
2. npm install vue
3. npm i -D webpack webpack-cli (-D는 개발환경에서만 사용하기 위한 옵션)
4. webpack.config.js \>\> webpack설정파일
    - export할 것들을 정의
    ```javascript
    module.exports = {
    // 파일들의 시작점
    entry: '',
    // webpack은 기본적으로 js만 변환가능 =\> css나 html을 이해할 수 있게 변환 내용작성
    module: {},
    // webpack을 통해서 번들된 결과를 추가 처리하는 부분(추가기능을 사용하고 싶다)
    plugins: {},
    // webpack을 통해서 번들된 결과물이 나올 곳
    output: {},
    }
    }
    ```
5. vue-loader, vue-template-compiler도 응용하기 위해 설치해준다.(html, vue파일을 변환해줌)
6. package.json 에서 scripts에 "build" : "webpack" 추가
    - 이것이 배포할 때 필요한 점

## 고려사항
- 이 후 html하나에서 가독성 좋게 사용
- 수정있으면 다시 빌드해야함
- webpack.confog.js에서 mode를 개발용으로 바꿔줘야 테스트 가능
- 모든 컴퍼넌트에는 한개의 최상위 태그만 존재
- js외에 파일은 loader류로 변환하게 해줘야함
    ```javascript
     module: {
    rules: [{
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      }
    ]
  },
  ```
- 파일구조는 본 디렉토리를 참조

## Vue 생성
- html에서 다루는 것과 다름 유의
```javascript
new Vue({
    render: (h) => h(App) // 최상위 component지정
  }).$mount('#app') // 어디에 작업 (#app인 태그에)
```