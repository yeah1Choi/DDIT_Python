import pymysql
class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root', 
            password='python', 
            db='python', 
            charset='utf8',
            port = 3305
        )
        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from emp"
        self.cur.execute(sql)
        
        list = self.cur.fetchall()
        return list
    
    def selectOne(self, e_id):
        sql = f"""
                select * from emp where e_id = {e_id}
            """
        self.cur.execute(sql)
        
        # vos = self.cur.fetchone()
        # return vos[0]   ## 이 방법도 있음..
        # fetchone : 배열의 [0]을 알아서 가져옴
        vo = self.cur.fetchone()
        return vo
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
                INSERT INTO emp VALUES ({e_id},{e_name},{gen},{addr})
            """
        cnt = self.cur.execute(sql)
        print(cnt)
        self.conn.commit()
    
    def delete(self, e_id):
        sql = f"""
                DELETE FROM emp 
                WHERE e_id = '{e_id}'
            """
        cnt = self.cur.execute(sql)
        print(cnt)
        self.conn.commit()
    
    def update(self, e_id, e_name, gen, addr):
        sql = f"""
                UPDATE emp 
                SET 
                    e_name = '{e_name}',
                    gen = '{gen}',
                    addr = '{addr}'
                WHERE e_id = '{e_id}'
            """
        cnt = self.cur.execute(sql)
        print(cnt)
        self.conn.commit()
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    vo = de.delete('5')
    print(vo)