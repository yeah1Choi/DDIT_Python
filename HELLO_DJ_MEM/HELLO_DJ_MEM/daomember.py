import pymysql
class DaoMember:
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
        sql = "select * from member"
        self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    def selectOne(self, m_id):
        sql = f"""
                select * from member where m_id = {m_id}
            """
        self.cur.execute(sql)
        vo = self.cur.fetchone()
        return vo
    
    def insert(self, m_id, m_name, tel, email):
        sql = f"""
                INSERT INTO member VALUES ({m_id},{m_name},{tel},{email})
            """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, m_id):
        sql = f"""
                DELETE FROM member 
                WHERE m_id = '{m_id}'
            """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, m_id, m_name, tel, email):
        sql = f"""
                UPDATE member 
                SET 
                    m_name = '{m_name}',
                    tel = '{tel}',
                    email = '{email}'
                WHERE m_id = '{m_id}'
            """
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoMember()