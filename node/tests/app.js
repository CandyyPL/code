const express = require('express');
const mysql = require('mysql');
const chalk = require('chalk');

const exp = express()

const data = {
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'nodedb'
};

const cnc = mysql.createConnection({
    host: data.host,
    user: data.user,
    password: data.password,
    database: data.database
});

cnc.connect((err) => {
    if(!err){
        console.log(`${chalk.green('[INFO]')} Created db connection`);
    }
    else{
        console.log(`${chalk.red('[ERROR]')} Failed to create db connection`);
    }
});

cnc.query(`SELECT * FROM ${data.database}`, (err, row, field) => {
    if(!err){
        // do something
    }
    else{
        console.log(`${chalk.red('[ERROR]')} Failed to execute db query`);
    }
});