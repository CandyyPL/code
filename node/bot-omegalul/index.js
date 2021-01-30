const Discord = require('discord.js')
const chalk = require('chalk')
const request = require('request')
const cheerio = require('cheerio')

const client = new Discord.Client()

const token = 'NzQ1NTg1MDQ1Mzg0ODU1NTg0.Xzz6Lw.U1_y40sQP2ZUulKQrs2D55OwOUk'
const prefix = '!'

const renderDate = () => {
    var tDay = new Date()

    var d = tDay.getDate()
    var m = tDay.getMonth()
    var y = tDay.getFullYear()

    var wd = tDay.getDay()

    var months = new Array(12)

    months[0] = ' stycznia '
    months[1] = ' lutego '
    months[2] = ' marca '
    months[3] = ' kwietnia '
    months[4] = ' maja '
    months[5] = ' czerwca '
    months[6] = ' lipca '
    months[7] = ' sierpnia '
    months[8] = ' września '
    months[9] = ' października '
    months[10] = ' listopada '
    months[11] = ' grudnia '

    var days = new Array(7)

    days[1] = 'poniedziałek, '
    days[2] = 'wtorek, '
    days[3] = 'środa, '
    days[4] = 'czwartek, '
    days[5] = 'piątek, '
    days[6] = 'sobota, '
    days[7] = 'niedziela, '

    return `Dzisiejszy dzień to ${days[wd]}${d}${months[m]}${y} roku`
}

const renderTime = () => {
    var tDay = new Date()

    var hrs = tDay.getHours()
    var min = tDay.getMinutes()

    if(min < 10) min = '0' + min

    return `Obecna godzina to ${hrs}:${min}`
}

const wastedOnLol = (user) => {
    console.log('function works')
    request(`https://wol.gg/stats/eune/${user}/`, (error, response, html) => {
        console.log('request done')
        if(!error && response.statusCode == 200){
            console.log('site ok')
            const site = cheerio.load(html)
            console.log('cheerio loaded site html')

            const element = site('#time-hours')
            console.log('found "#time-hours" element')
            const hrs = element.find('p').text()
            console.log('found hours segment')

            console.log(hrs)
            console.log(hrs.slice(0, -5))

            return `Gracz ${user} spędził w League of Legends ${hrs.slice(0, -5)} godzin`
        }
    })
}

client.on('ready', () => {
    console.log(`[${chalk.green('INFO')}] Logged in as ${client.user.tag}`)
})

client.on('message', (msg) => {
    if(!msg.guild){
        console.log(`[${chalk.red('PRIVATE MESSAGE')}] ${msg.author.tag} | ${msg.content}`)
        return
    }
    else if(!msg.author.bot){
        console.log(`[${chalk.yellow('INFO')}] ${msg.author.tag} | ${msg.content}`)

        if(msg.content === `${prefix}date`){
            msg.channel.send(renderDate())
        }

        if(msg.content === `${prefix}time`){
            msg.channel.send(renderTime())
        }

        if(msg.content.startsWith(`${prefix}wol `)){
            const user = msg.content.slice(5)
            if(user != null){
                const hours = wastedOnLol(user)
                console.log(hours)
                if(hours != null){
                    msg.channel.send(hours)
                }
            }
        }
    }
})

client.login(token)