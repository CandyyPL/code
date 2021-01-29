const mongo = require('mongoose')
require('dotenv/config')

const url = process.env.DB_CONNECTION

mongo.connect(url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}, () => {
    console.log('Connected to DB')
})