import pymysql

class MyEmpDao:
    def __init__(self, host="localhost", user="root", password="mysql",db="flask", port=33066, charset="utf8"):
        self.db = pymysql.connect(host=host, user=user, password=password, db=db, port=port, charset=charset) 
    
    def getEmps(self):
        ret = []
        # db = pymysql.connect(host='localhost', user='root', db='flask', password='mysql', charset='utf8')
        curs = self.db.cursor()
        
        sql = "select * from emp"
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            temp = {'empno':e[0],'name':e[1],'department':e[2],'phone':e[3] }
            ret.append(temp)
        
        self.db.commit()
        # self.db.close()
        return ret
    
    def insEmp(self, empno, name, department, phone):
        # db = pymysql.connect(host='localhost', user='root', db='flask', password='mysql', charset='utf8')
        curs = self.db.cursor()
        
        sql = '''insert into emp (empno, name, department, phone) values (%s,%s,%s,%s)'''
        curs.execute(sql,(empno, name, department, phone))
        self.db.commit()
    
    def updEmp(self, empno, name, department, phone): 
        # db = pymysql.connect(host='localhost', user='root', db='flask', password='mysql', charset='utf8')
        curs = self.db.cursor()
        
        sql = "update emp set name=%s, department=%s, phone=%s where empno=%s"
        curs.execute(sql, (name, department, phone, empno))
        self.db.commit()
        
    def delEmp(self, empno):
        # db = pymysql.connect(host='localhost', user='root', db='python', password='python', charset='utf8')
        curs = self.db.cursor()
        
        sql = "delete from emp where empno=%s"
        curs.execute(sql,empno)
        self.db.commit()

if __name__ == '__main__':
    # MyEmpDao().insEmp('0000', 'kim', 'IT', '+8210-1234-5678')
    #MyEmpDao().updEmp('aa', 'dd', 'dd', 'aa')
    emplist = MyEmpDao().getEmps()
    print(emplist)