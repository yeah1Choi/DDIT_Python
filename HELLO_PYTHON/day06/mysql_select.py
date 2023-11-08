import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    user='root', 
    password='python', 
    db='python', 
    charset='utf8',
    port = 3305
)
cur = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * from emp"
cur.execute(sql)

rows = cur.fetchall()
print(rows)

cur.close()
conn.close()