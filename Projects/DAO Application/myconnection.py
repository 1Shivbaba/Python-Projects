" Make connection wit database"

import  MySQLdb

class MyConnect:
    @staticmethod
    def getConnection():
        con = MySQLdb.connect(host="localhost", user="root", password="shivbaba", database="shivam")
        return con
