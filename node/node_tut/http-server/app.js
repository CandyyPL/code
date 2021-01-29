const http = require('http')

const handler = (request, response) => {
    console.log('new user')
    response.end('hello world')
}

const server = http.createServer(handler)
const port = 3000

server.listen(port, (err) => {
    if(err){
        return console.log('something went wrong')
    }

    console.log('ok')
})