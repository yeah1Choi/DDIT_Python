var Mysql = require('sync-mysql');

var connection = new Mysql({  // mysql 접속 설정
    host: 'localhost',
    port: '3305',
    user: 'root',
    password: 'python',
    database: 'python'
});

var e_id = '2';
var e_name = '2';
var gen = '2';
var addr = '2';

var sql = `insert into emp (e_id,e_name,gen,addr) values ('${e_id}','${e_name}','${gen}','${addr}');`;
 
var result = connection.query(sql);

console.log(result); 
connection.dispose();