const mysql = require('mysql');  // mysql 모듈 로드
const conn = {  // mysql 접속 설정
    host: 'localhost',
    port: '3305',
    user: 'root',
    password: 'python',
    database: 'python'
};

var e_id = '3';

let connection = mysql.createConnection(conn); // DB 커넥션 생성
connection.connect();   // DB 접속

sql = `delete from emp where e_id='${e_id}'`;
 
connection.query(sql, function (err, results, fields) { 
    if (err) {
        console.log(err);
    }
    console.log(results.affectedRows);
});
 
 
connection.end(); // DB 접속 종료