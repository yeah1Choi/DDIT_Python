var Mysql = require('sync-mysql');

var connection = new Mysql({  // mysql 접속 설정
    host: 'localhost',
    port: '3305',
    user: 'root',
    password: 'python',
    database: 'python'
});

var e_id = '2';
var e_name = '4';
var gen = '4';
var addr = '4';

var sql = `update emp set e_name='${e_name}', gen='${gen}', addr='${addr}' where e_id='${e_id}'`;
 
var result = connection.query(sql);

console.log(result); 
connection.dispose();