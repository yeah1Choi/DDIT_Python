var Mysql = require('sync-mysql');

var connection = new Mysql({  // mysql 접속 설정
    host: 'localhost',
    port: '3305',
    user: 'root',
    password: 'python',
    database: 'python'
});

var sql = `SELECT * FROM emp`;
 
var result = connection.query(sql);
 

console.log(result); 
connection.dispose();