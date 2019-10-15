#codign=utf-8

import pymysql
import readConf


mysql=readConf

class MysalDb():
    dataname='xp-testDATABASE'
    def __init__(self):
        self.host = mysql.getvalue(self.dataname,'host')
        self.user = mysql.getvalue(self.dataname,'user')
        self.passwd = mysql.getvalue(self.dataname,'passwd')
        self.database = mysql.getvalue(self.dataname,'database')
        self.port = mysql.getvalue(self.dataname,'port')
        self.db = pymysql.connect(host=self.host,
                                  port=int(self.port),
                                  user=self.user,
                                  passwd=self.passwd,
                                  db=self.database,charset="utf8")

    def query_db(self,sql):
        '''数据库查询'''
        cur = self.db.cursor()
        cur.execute(sql) # db.commit()提交到数据库执行
        data = cur.fetchall()
        print(data)
        self.db.close()
        return data

    def delete_db(self,sql_delete):
        cur = self.db.cursor()

        try:
            cur.execute(sql_delete)
            self.db.commit()
        except Exception as e:
            print("操作异常：%s" % str(e))
            # 错误回滚
            self.db.rollback()

        finally:
            self.db.close()


wh=MysalDb()
wh.query_db("SELECT * FROM dp_code WHERE identify_code='1111'")

