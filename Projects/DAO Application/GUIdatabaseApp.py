
"Python Program on GUI Applications with PDBC"

from tkinter import *
import tkinter.messagebox as msg
import  tkinter.simpledialog as sd
import  employeedao as ed
import model

def click(event):

    if(event=='save'):
        E = model.Employee()
        E.setid(empid.get())
        E.setname(empname.get())
        E.setdept(empdept.get())
        E.setsalary(empsal.get())
        Em = ed.EmployeeDAO()
        choice = msg.askyesno("Save ", "Are you sure want to save ?")
        if (choice == True):
            Em.insertEmp(E)

    elif (event == 'delete'):
        id = sd.askinteger("Delete window", "Enter Employee ID : ")
        E = ed.EmployeeDAO()
        A = E.searchEmployee(id)
        if (A != None):
            empid.set(A.getid())
            empname.set(A.getname())
            empdept.set(A.getdept())
            empsal.set(A.getsalary())
            ch=msg.askyesno("Delete ", "Are you sure want to delete?")
            if(ch==True):
                E.deleteEmployee(id)
                empid.set(" ")
                empname.set(" ")
                empdept.set(" ")
                empsal.set(" " )
                msg.showinfo("Delete", "Record Deleted!")
        else:
            msg.showerror("No Record", "No Record Found !")

    elif (event == 'update'):
        print("Update")

    elif (event == 'search'):
       id=sd.askinteger("Search", "Enter Employee ID : ")
       E = ed.EmployeeDAO()
       A= E.searchEmployee(id)
       if(A!=None):
           empid.set(A.getid())
           empname.set(A.getname())
           empdept.set(A.getdept())
           empsal.set(A.getsalary())
       else:
           msg.showerror("No Record","No Record Found !")

    elif (event == 'exit'):
        choice = msg.askyesno("Exit ","Are you sure want to exit ?")
        if (choice==True):
            myroot.destroy()

myroot=Tk()
myroot.geometry('100x100')
myroot.maxsize(600,600)
myroot.minsize(600,600)
myroot.title("Employee Registration Form")
myroot.wm_iconbitmap('emp.ico')
lb1=Label(text="Enter Employee Id:",font=('Arial,10.bold'),fg="red")
lb1.grid(row=0,column=0)
empid=IntVar()
txtid=Entry(textvariable=empid,font=('Arial,10.bold'),fg="blue")
txtid.grid(row=0,column=1)
lb1=Label(text="Enter Name:",font=('Arial,10.bold'),fg="red")
lb1.grid(row=1,column=0)
empname=StringVar()
txtname=Entry(textvariable=empname,font=('Arial,10.bold'),fg="blue")
txtname.grid(row=1,column=1)
lb3=Label(text="Enter Department:",font=('Arial,10.bold'),fg="red")
lb3.grid(row=3,column=0)
empdept=StringVar()
txtdept=Entry(textvariable=empdept,font=('Arial,10.bold'),fg="blue")
txtdept.grid(row=3,column=1)
lb4=Label(text="Enter Salary:",font=('Arial,10.bold'),fg="red")
lb4.grid(row=4,column=0)
lb5=Label(text="  ",font=('Arial,20,bold'),fg="green")
lb5.grid(row=8,column=1)
empsal=IntVar()
txtsal=Entry(textvariable=empsal,font=('Arial,10.bold'),fg="blue")
txtsal.grid(row=4,column=1)
txtsal.bind('<Return>',click)
btnsave=Button(text='Save',font=('Verdana,10.bold'),fg="black",command=lambda :click('save'))
btnsave.grid(row=5,column=1)
btndelete=Button(text='Delete',font=('Verdana,10.bold'),fg="black",command=lambda :click('delete'))
btndelete.grid(row=5,column=0)
btnserch=Button(text='Search',font=('Verdana,10.bold'),fg="black",command=lambda :click('search'))
btnserch.grid(row=5,column=2)
btnupdate=Button(text='Update',font=('Verdana,10.bold'),fg="black",command=lambda :click('update'))
btnupdate.place(x= 110, y = 99)
btnexit=Button(text='Exit',font=('Verdana,10.bold'),fg="black",command=lambda :click('exit'))
btnexit.place(x= 170, y = 140)

myroot.mainloop()