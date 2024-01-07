import myconnection as ms
import model
import employeedao as ed

E1 = ed.EmployeeDAO()
myliset1=E1.searchAll()
print(" Emp ID              EName               EDep            Esalary ")
for em in myliset1:
    print("-------------------------------------------------------------")
    # print(em.getid(),end="                  ")
    # print(em.getname(), end="            ")
    # print(em.getdept(), end="                ")
    # print(em.getsalary(), end="                  ")
    print(" %d              %s                %s                  %d"%(em.getid(),em.getname(), em.getdept(), em.getsalary()))





#RECORD UPDATE CODE
# E1 = model.Employee()
# eid = int(input("Enter emp ID: "))
# ename = input("Enter emp name for update: ")
# edept = input("Enter emp department for update: ")
# esal = int(input("Enter emp salary for update: "))
# E1.setid(eid)
# E1.setname(ename)
# E1.setdept(edept)
# E1.setsalary(esal)
# Emd = ed.EmployeeDAO()
# Emd.updateEmplyee(E1)
# print("Record Updated....")


# DELETE CODE
# emid = int(input("Enter Employee ID for Delete : "))
# Emd = ed.EmployeeDAO()
# E  = Emd.searchEmployee(emid)
# if (E==None):
#     print("----------No Record Found----------")
# else:
#     print("Employee Id :", E.getid())
#     print("Employee name: " ,E.getname())
#     print("Employee Department: ", E.getdept())
#     print("Employee Salary:  ", E.getsalary())
#     choice = input("Are sure want to delete this id (yes/no): ")
#     if(choice=="yes"):
#         Emd.deleteEmployee(emid)
#         print("Record Deleted..........")



#
# E1.setid(104)
# E1.setname("Rashmi ")
# E1.setdept("CSE")
# E1.setsalary(50000)
#
# Emp.insertEmp(E1)


