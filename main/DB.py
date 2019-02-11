# coding:utf-8
# 数据库接口
import mysql.connector
class conndb:
    def __init__(self, data=None, data_all=None):
        self.data = data
        self.data_all = data_all
        self.data_query = []
        try:
            self.mydb = mysql.connector.connect(
                host= 'localhost',
                user= 'root',
                password= 'dsong',
                db= 'test'
                )
        except:
            print('数据库链接失败！')
        self.mysursor = self.mydb.cursor()

    def db_insert(self):
        
        '''插入新的记录,data为剩余可用，data_all为所有已用
        '''
        try:
            self.mysursor.execute("INSERT INTO query (OVER, use_all) VALUES ('{}', '{}');".format(self.data, self.data_all))
            self.mydb.commit()
        except:
            print('记录失败！')

    def query_db(self):
        '''查询历史记录
        '''
        try:
            self.mysursor.execute("SELECT OVER, use_all from query")
            result = self.mysursor.fetchall()
            self.mydb.close()
        except:
            print('查询失败')
        for row in result:
            li = {}
            li['剩余'] = row[0]
            li['已用'] = row[1]
            self.data_query.append(li)
        return self.data_query
    
