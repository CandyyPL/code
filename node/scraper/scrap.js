const request = require('request');
const cheerio = require('cheerio');

request('https://wol.gg/stats/eune/candyyq/', (error, response, html) => {
    if(!error && response.statusCode == 200){
        const site = cheerio.load(html);

        const element = site('#time-hours');
        const hrs = element.find('p').text();

        console.log(hrs.slice(0, -5));
    }
});