require('./db_init')
const User = require('./models/User')

const createUser = async (data) => {
    try{
        const user = new User(data)
        await user.save()

        console.log(user)
    } catch (error){
        console.log('Something went wrong ', error)
    }

}

const findUsers = async () => {
    try{
        const users = await User.find({})

        console.log(users)
    } catch (error){
        console.log('Something went wrong ', error)
    }
}

createUser({ name: 'Alice', age: 17 })
// findUsers()