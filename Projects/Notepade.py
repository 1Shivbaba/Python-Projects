"Notepad application"

from tkinter import *
import tkinter.messagebox as  msgbox
import tkinter.filedialog as fd
def menuclick(choice):
   textbox = Text(myroot, width=1200, height=500, font=('Arial', 15, 'bold'),wrap=WORD)

   if(choice=='new'):
       textbox.pack()
   elif(choice=='newwindow'):
       filename = fd.askopenfilename(parent=myroot, title='open file window'
                                     ,filetypes=(("Text File", "*.txt"), ("All File", "*.*")))
       f=open(filename, 'r')
       mytext=f.read()
       textbox1=Text(myroot, width=1200, height=500, font=('Arial', 15, 'bold'), wrap=WORD)
       textbox1.pack()
       textbox1.insert(1.0, mytext)
       f.close()

   elif (choice == 'save'):
       textbox=Text(myroot,width=1200,height=500,font=('Arial',15,'bold'))
       textbox.pack()
       filename=fd.asksaveasfilename(parent=myroot,defaultextension='*.txt')
       containt = str(textbox.get(1.0,END))
       f=open(filename,'w')
       f.write(containt)
       f.close()
   elif (choice == 'saveas'):
       textbox=Text(myroot,width=1200,height=500,font=('Arial',15,'bold'))
       textbox.pack()
       filename=fd.asksaveasfilename(parent=myroot,defaultextension='*.txt')
       containt = str(textbox.get(1.0,END))
       f=open(filename,'w')
       f.write(containt)
       f.close()
   elif(choice=='exit'):
       ch=msgbox.askyesno('exit','Are you sure want to exit')
       if(ch==True):
           myroot.destroy()


myroot=Tk()
myroot.geometry('1200x500')
myroot.title("Notepad")
myroot.wm_iconbitmap('app.ico')
menubar=Menu(myroot)
myroot.config(menu=menubar)
filemenu=Menu(myroot,tearoff=0)
filemenu.add_command(label="New",accelerator='Ctrl+N',command=lambda :menuclick('new'))
filemenu.add_command(label="New Window",accelerator='Ctrl+Shift+N',command=lambda :menuclick('newwindow'))
filemenu.add_command(label="Save",accelerator='Ctrl+S',command=lambda :menuclick('save'))
filemenu.add_command(label="Save As.",accelerator='Ctrl+Shift+S',command=lambda :menuclick('saveas'))
filemenu.add_separator()
filemenu.add_command(label="Page Setup",accelerator='Ctrl+S',command=lambda :menuclick('pagesetup'))
filemenu.add_command(label="Print",accelerator='Ctrl+Shift+S',command=lambda :menuclick('print'))
filemenu.add_command(label="Exit",accelerator='Ctrl+Q',command=lambda :menuclick('exit'))
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(myroot,tearoff=0)
editmenu.add_command(label="Cut",accelerator='Ctrl+X')
editmenu.add_command(label="Copy",accelerator='Ctrl+C')
editmenu.add_command(label="Paste",accelerator='Ctrl+V')
editmenu.add_command(label="Delete",accelerator='Del')
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Find Next")
editmenu.add_command(label="Find Previous")
editmenu.add_command(label="Replace")
editmenu.add_command(label="Goto")
menubar.add_cascade(label='Edit',menu=editmenu)

myroot.mainloop()