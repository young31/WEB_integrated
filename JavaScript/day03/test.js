const url = 'https://jsonplaceholder.typicode.com/posts'
const XHR = new XMLHttpRequest()

XHR.open('GET', url)

XHR.addEventListener('load', function(event) {
  console.log(event)
})

XHR.send()