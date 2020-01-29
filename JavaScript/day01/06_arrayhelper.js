const num2 = [4, 9, 16]

const sqrt = (num) => Math.sqrt(num)
console.log(num2.map(sqrt))


const products = [
    { name: 'banana', type: 'fruit' },
    { name: 'cu', type: 'vege' },
    { name: 'apple', type: 'fruit' },
    { name: 'ca', type: 'vege' },
]
let fruit = function(product) {
    return product.type === 'fruit'
}
console.log(products.filter(fruit))


const trips = [
  { distance: 34, time: 10 },
  { distance: 90, time: 50 },
  { distance: 59, time: 25 },
]

const speed = (obj) => obj.distance/obj.time
const item = item => item>= 2
console.log(trips.map(speed).filter(item))


const ages = [15, 25, 35, 45, 55, 65, 75, 85, 95]
const oldAges = ages.filter(age => (age>=50))
const complex = ages.map(age => (age+10)).filter(age => (age >= 50))
console.log(oldAges)
console.log(complex)


const users = [
  { name: 'tony', age: 43 },
  { name: 'steve', age: 32 },
  { name: 'thor', age: 40 },
]

console.log(users.find(user => (user.name === 'tony')))


const arr = [1, 2, 3, 4, 5]
console.log(arr.some(n => (n%2 === 0)))
console.log(arr.every(n => (n%2 === 0)))


const requests = [
  { url:'/photos', status: 'complete' },
  { url: '/albums', status: 'pending'},
  { url: '/users', status: 'failed' }
]

console.log(requests.some((obj) => (obj.status === 'pending')))


const scores = [90, 99, 79, 88]

const sum = scores.reduce((total, score) => {
  total += score
  return total // 누적 값 넘김
},
0
)

const doublescores = scores.reduce((target, score) => {
  target.push(score*2)
  return target
},
[]
)
console.log(doublescores)

let ls = [1,2,3,4]
let r = 4
let aa
let bb
const perm = function (k) {
  if (k === r) {
    console.log(ls)
  } else {
    for (let i=k; i<r; i++) {
      aa = ls[i]
      bb = ls[k]
      ls[k] = aa
      ls[i] = bb
      perm(k+1)
      aa = ls[i]
      bb = ls[k]
      ls[k] = bb
      ls[i] = aa
    }
  }
}

perm(0)