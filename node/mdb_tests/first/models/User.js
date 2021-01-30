const mongo = require('mongoose')

const userSchema = new mongo.Schema({
    name: {
        type: String,
        required: true
    },
    age: {
        type: Number,
        required: true,
        min: 18
    }
})

const User = mongo.model('User', userSchema)

module.exports = User