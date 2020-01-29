function sleep_3() {
  setTimeout(function() {
    console.log('wake up')
  }, 3000)
}

console.log('sleep')
sleep_3()
console.log('end')