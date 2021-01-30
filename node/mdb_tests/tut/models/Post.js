const mongo = require('mongoose')

const postSchema = new mongo.Schema({
    title: {
        type: String,
        required: true
    },
    description: {
        content: String,
        required: true
    },
    author: {
        type: String,
        required: true
    }
})

const Post = mongo.model('Post', postSchema)

module.exports = Post