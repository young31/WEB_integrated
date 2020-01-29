const username = prompt('hello')

let meassage = ''

if (username === 'ssafy') {
    message = '<h1>hi</h1>'
} else if (username === 'ss') {
    message = '<h2>else if</h2>'
} else {
    message = '<h3>else </h3>'
}

document.write(message)