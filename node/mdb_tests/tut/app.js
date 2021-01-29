const express = require('express')
const app = express()

require('./db-init')

const postsRoute = require('./routes/posts')

app.use('/posts', postsRoute)

app.get('/', (req, res) => {
    res.send('We are on home')
})

app.listen(3000)