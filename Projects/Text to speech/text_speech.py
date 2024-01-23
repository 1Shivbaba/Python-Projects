## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound

def Text_to_speech():
    try:
        Message = entry_field.get()
        speech = gTTS(text = Message)
        speech.save('speach.mp3')
        playsound('speach.mp3')
    except Exception as msg:
        print(msg)

def Exit():
    root.destroy()

def Reset():
    Msg.set("")


################### Initialized window####################

root = Tk()

root.geometry('350x300')
root.wm_iconbitmap('ts.ico')
root.resizable(False, False)
root.config(bg = 'ghost white')
root.title(' TEXT_TO_SPEECH App')
root.configure(bg='sky blue')

##heading
Label(root, text = 'TEXT_TO_SPEECH' , font='arial 20 bold' , bg ='sky blue').pack()
Label(root, text ='Developed by Shivam Ojha ' , font ='arial 15 bold', bg = 'sky blue').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='sky blue').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width =50)
entry_field.place(x=20 , y=100)


###################define function##############################


#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, width =4, activebackground='green').place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1', activebackground='green').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, activebackground='green').place(x=175 , y =140)


#infinite loop to run program
root.mainloop()
