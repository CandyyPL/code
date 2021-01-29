const mongo = require('mongoose')

const url = 'mongodb://127.0.0.1:27017/mdb-test'

mongo.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})