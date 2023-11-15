const mysql = require('mysql');  // mysql 모듈 로드
const conn = {  // mysql 접속 설정
    host: 'localhost',
    port: '3305',
    user: 'root',
    password: 'python',
    database: 'python'
};

let connection = mysql.createConnection(conn); // DB 커넥션 생성
connection.connect();   // DB 접속
 
sql = "SELECT * FROM emp";
 
connection.query(sql, function (err, results, fields) { 
    if (err) {
        console.log(err);
    }
    console.log(results);
});
 
 
connection.end(); // DB 접속 종료