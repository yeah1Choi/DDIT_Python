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

e_id = "6"
e_name = "6"
gen = "6"
addr = "6"

sql = f"""
    UPDATE emp 
    SET 
        e_id = '{e_id}',
        e_name = '{e_name}',
        gen = '{gen}',
        addr = '{addr}'
    WHERE e_id = '5'
    """
cnt = cur.execute(sql)

print(cnt)

conn.commit()

cur.close()
conn.close()