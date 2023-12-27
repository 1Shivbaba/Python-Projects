"Python Program to Create Login Application in GUI"

from tkinter import *
def checkLogin():
    # print("User Name:",uname.get())
    # print("Password:", upass.get())
    #     user=uname.get()
    #     pass1=upass.get()
        if(uname.get()=='shivam123' and upass.get()=='Password'):
               lb3["text"]="Valid User"
               lb3["fg"]="green"

        else:
              lb3["text"]="Invalid User .. Login again"
              lb3["fg"] = "red"

my_root=Tk()
my_root.title("Login Window")
my_root.geometry('400x200')
my_root.wm_iconbitmap('app.ico')
my_root.maxsize(400,200)
my_root.minsize(400,200)

lb1=Label(text="User Name:",fg='blue',font=('Arial',10,'bold'))
lb2=Label(text="Password:",fg='blue',font=('Arial',10,'bold'))
lb3=Label(text="-",font=('Arial',10,'bold'))

lb1.grid(row=0,column=0)
lb2.grid(row=1,column=0)
lb3.grid(row=2,column=0)

uname=StringVar()
upass=StringVar()
txtuser=Entry(textvariable=uname,font=('Arial',10,'bold'),fg='red')
txtpass=Entry(textvariable=upass,font=('Arial',10,'bold'),fg='red',show='*')

txtuser.grid(row=0,column=1)
txtpass.grid(row=1,column=1)

btn1=Button(text="Login",font=('Arial',10,'bold'),fg='#A52A2A',command=checkLogin)
btn1.grid(row=3,column=0)

my_root.mainloop()