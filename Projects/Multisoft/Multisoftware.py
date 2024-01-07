"Python Program to Open Multiple Software Using GUI Application Tkinter"

from tkinter import *
import os

def opencalc():
   os.system("calc")
def openpaintb():
    os.system("mspaint")
def openword():
    os.system("start winword.exe")
def openexcel():
    os.system("start excel.exe")
def openpower():
    os.system("start powerpnt.exe")
def opennotepad():
    os.system("notepad")
def opendate():
    os.system("date")

myroot=Tk()
myroot.geometry('300x300')
myroot.minsize(300,300)
myroot.maxsize(600,600)
myroot.title("Multiple Software in One App")
myroot.wm_iconbitmap('mult.ico')
menubar=Menu(myroot)
myroot.config(menu=menubar)
filemenu=Menu(myroot,tearoff=0)
filemenu.add_command(label="NotePad",command=opennotepad)
filemenu.add_command(label="Date",command=opendate)
filemenu.add_command(label="Calculator",command=opencalc)
filemenu.add_command(label="MS Paint",command=openpaintb)
filemenu.add_command(label="MS Word",command=openword)
filemenu.add_command(label="MS Excel",command=openexcel)
filemenu.add_command(label="MS Power Point",command=openpower)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=myroot.destroy)
menubar.add_cascade(label='Software',menu=filemenu)

editmenu=Menu(myroot,tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_separator()
menubar.add_cascade(label='Edit',menu=editmenu)
myroot.mainloop()