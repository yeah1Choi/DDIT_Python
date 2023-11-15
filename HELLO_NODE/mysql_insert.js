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

console.log("start");
 
sql = "insert into emp (`e_id`,`e_name`,`gen`,`addr`) values (5,5,5,5);";
 /* 쓰레드라서 비동기 방식으로 기다렸다가 마지막으로 출력이 되는 것이다 */
connection.query(sql, function (err, results, fields) { 
    if (err) {
        console.log(err);
    }
    console.log(results.affectedRows);
});
connection.end(); // DB 접속 종료

console.log("end");
