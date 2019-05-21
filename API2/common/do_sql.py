import pymysql

class DoMysql:

    host = '120.24.235.105'
    user = 'python'
    password = 'python666'
    port = 3306
    mysql = pymysql.connect(host=host,user=user,
                            password=password,port=port)
    cursor = mysql.cursor()

    def get_fetchone(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def get_fetchall(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
    sql = 'select Fverify_code from sms_db_24.t_mvcode_info_9 where Fmobile_no =18258129924'
    domysql = DoMysql().get_fetchone(sql)
    print(domysql)
    DoMysql().close()
