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

sql = f"""
    DELETE FROM emp 
    WHERE e_id = '6'
    """
cnt = cur.execute(sql)

print(cnt)

conn.commit()

cur.close()
conn.close()