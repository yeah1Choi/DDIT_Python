import pymysql
class DaoStudent:
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
        sql = "select * from student"
        self.cur.execute(sql)
        students = self.cur.fetchall()
        return students
    
    def selectOne(self, s_id):
        sql = f"""
        select * from student where s_id = {s_id}
        """
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return vo
    
    def insert(self, s_id, s_name, mobile, grade):
        sql = f"""
                INSERT INTO student VALUES ({s_id},{s_name},{mobile},{grade})
            """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, s_id):
        sql = f"""
                DELETE FROM student 
                WHERE s_id = '{s_id}'
            """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, s_id, s_name, mobile, grade):
        sql = f"""
                UPDATE student 
                SET 
                    s_name = '{s_name}',
                    mobile = '{mobile}',
                    grade = '{grade}'
                WHERE s_id = '{s_id}'
            """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    ds = DaoStudent()