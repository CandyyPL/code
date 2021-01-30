const express = require('express')

const app = express()
app.set('view engine', 'hbs')

app.get('/', function (req, res){
    res.render('index', {
        pageTitle: 'Node.js Site',
        pageBody: 'Hello node'
    })
})

app.listen(3000)