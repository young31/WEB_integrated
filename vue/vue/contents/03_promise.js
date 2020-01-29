// 일반
function getData() {
  let data

  setTimeout(() => {
    console.log('INFO:요청보냄')
    data = { data: 'somedata' }
  }, 100);
  return data
}

function printData() {
  let request = getData()
  console.log(request)
}

printData()
console.log('-------------')


// callback활용
function getDataCallback(callback) {
  setTimeout(() => {
    console.log('INFO: request')
    const data = { data: 'somedata' }
    callback(data)
  }, 100)
}

getDataCallback(function(data) {
  console.log(data)
})
console.log('-------------')


// promise
function getDataPromise() {
  // 하는일은 promise를 리턴하는 것만 함 => 어떤 promise?
  // 이런 것이 axios 스타일
  return new Promise(resolve => { // resolve는 promise제공 함수

    setTimeout(() => {
      console.log('INFO: request')
      const data = { data: 'somedata' }
      resolve(data) // .then으로 꺼낼 수 있는 객체
    }, 100);
  })

}

console.log(getDataPromise())
getDataPromise()
  .then(response => {
    console.log(response)
  })


console.log('-------------')
const handleData = async function() {
  const response = await getDataPromise()
  console.log(response)
}

console.log('-------------')
async function printData() {
  const data = await getDataPromise()
  console.log(data)
}

////////////// 비동기식 vs 동기식 같은 결과 코드 ////////////////
const API_URL = 'https://dog.ceo/api/breeds/image/random'
axios.get(API_URL)
  .then((response) => {
    console.log(response)
  })

const getImage = async function() {
    const response = await axios.get(API_URL) // 기다리는 것이 아니라 오는것 기다렸다가 같이 보겠다.
    console.log(reponse)
  }
  /////////////////////////////////////////////////////////////