import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    user='root', 
    password='python', 
    db='python', 
    charset='utf8',
    port = 3305
)

e_id = "5"
e_name = "5"
gen = "5"
addr = "5"

cur = conn.cursor()

sql = f"""
    INSERT INTO emp 
    (e_id, e_name, gen, addr)
    VALUES ('{e_id}','{e_name}','{gen}','{addr}')
"""
cnt = cur.execute(sql)

print(cnt)

conn.commit()

cur.close()
conn.close()