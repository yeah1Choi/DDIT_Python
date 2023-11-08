import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    user='root', 
    password='python', 
    db='python', 
    charset='utf8',
    port = 3305
)
cur = conn.cursor()

sql = "INSERT INTO emp VALUES (%s,%s,%s,%s)"
val = ("4","4","4","4")
cur.execute(sql, val)

conn.commit()

cur.close()
conn.close()