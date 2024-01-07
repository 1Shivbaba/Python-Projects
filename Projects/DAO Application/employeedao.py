import model
import myconnection as ms


class EmployeeDAO:

    def __init__(self):
        self.con = ms.MyConnect.getConnection()
        self.cur = self.con.cursor()
        print("Connection Success")

    def insertEmp(self, E):
        try:
            sql = "insert into employee values( '%d', '%s', '%s', '%d')"
            value = (E.getid(), E.getname(), E.getdept(), E.getsalary())
            self.cur.execute(sql % value)
            self.con.commit()
            print("Record Inserted", self.cur.rowcount)

        except Exception as obj:
            print(obj)

    def searchAll(self):
        mylist = [ ]
        try:
            sql = "select * from employee"
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for row in result:
                E1 = model.Employee()
                E1.setid(row[0])
                E1.setname(row[1])
                E1.setdept(row[2])
                E1.setsalary(row[3])
                mylist.append(E1)
            return mylist
        except Exception as ob:
            print(ob)
    def searchEmployee(self, empid):
        try:
            sql = "select * from employee where eid = %d"
            self.cur.execute(sql % empid)
            r = self.cur.fetchone()
            if(self.cur.rowcount>0):
                E1 = model.Employee()
                E1.setid(r[0])
                E1.setname(r[1])
                E1.setdept(r[2])
                E1.setsalary(r[3])
                return E1
            else:
                E1 = None
                return E1
        except Exception as msg:
            print(msg)

    def deleteEmployee(self, empid):
        sql = "delete from employee where eid = %d"
        self.cur.execute(sql % empid)
        self.con.commit()

    def updateEmplyee(self,E):
        sql= "update employee set ename= '%s' , dept = '%s', Salary='%d' where eid= '%d' "
        value = (E.getname(), E.getdept(), E.getsalary(), E.getid() )
        self.cur.execute(sql % value)
        self.con.commit()



    def __del__(self):
        self.con.close()
        print("Connection Closed .......")