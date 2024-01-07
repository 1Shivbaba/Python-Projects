#**********************Music Player***********************
from tkinter import *
from tkinter import filedialog
from pygame import  mixer
from tkinter.ttk import Progressbar
import  datetime
from mutagen.mp3 import MP3



def introLable():
    global  text, a
    if(a>=len(s)):
        a = -1
        text = ' '
        L3.configure(text=text)
    else:
        text = text+s[a]
        L3.configure(text=text)
    a += 1
    L3.after(150, introLable)

currentvol = 0
def click(event):

    if (event=='search'):

        try:
            a = filedialog.askopenfilename( initialdir='D:\Drill & music',
                                            title='Select Music File', filetypes=(('MP3' ,'*.mp3'),('WAV','*.wav')))
        except Exception as ob:
            a = filedialog.askopenfilename(initialdir='D:\Drill & music',
                                           title='Select Music File', filetypes=(('MP3', '*.mp3'), ('WAV', '*.wav')))
            print(ob)
        track.set(a)
        m = track.get()
        mixer.music.load(m)
        mixer.music.play()
        mixer.music.set_volume(0.21)
        Pvalue.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
        Pr1['value'] = mixer.music.get_volume() * 100
        PL1.grid()
        PL2.grid()
        root.Mute.place(x=830, y=250)
        progress()

        song= MP3(a)
        songlenght = int(song.info.length)
        Prmusic['maximum'] = songlenght
        PLend.configure(text= '{}'.format(str(datetime.timedelta(seconds=songlenght))))

    elif (event=='play'):
        m = track.get()
        mixer.music.load(m)
        mixer.music.play()
        L2.configure(text="Playing........")

    elif(event=='stop'):
        mixer.music.stop()
        L2.configure(text="Stoped........")


    elif(event=='pause'):
        mixer.music.pause()
        root.pause.grid_remove()
        root.resume.grid()
        L2.configure(text="Paused....")

    elif(event=='resume'):
        root.resume.grid_remove()
        root.pause.grid()
        mixer.music.unpause()
        L2.configure(text="Playing........")

    elif (event == 'vup'):
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol+0.05)
        Pvalue.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
        Pr1['value'] = mixer.music.get_volume() * 100

    elif (event == 'vdown'):
        vol = mixer.music.get_volume()
        mixer.music.set_volume(vol - 0.05)
        Pvalue.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
        Pr1['value'] = mixer.music.get_volume() * 100

    elif (event == 'mute'):
        global currentvol
        root.Mute.place_forget()
        root.Unmute.place(x=830,y=250)
        currentvol= mixer.music.get_volume()
        mixer.music.set_volume(0)
        L2.configure(text="Muted........")


    elif(event=='unmute'):

        root.Mute.place(x=830, y=250)
        root.Unmute.place_forget()
        mixer.music.set_volume(currentvol)
        L2.configure(text="Unmuted........")

def progress():
    current = mixer.music.get_pos()//1000
    Prmusic['value'] = current
    Prmusic.after(2, progress)
    PLstart.configure(text='{}'.format(str(datetime.timedelta(seconds=current))))

root = Tk()
root.geometry('930x400+200+50')
root.title(" 'S'  Music Player")
root.wm_iconbitmap('music.ico')
root.resizable(False,False)
root.configure(bg='sky blue')


"***************************************************Music  Progressbar*****"
songlenght= 0

PL2= Label(root,text=' ', background= 'red')
PL2.grid(row= 3, column=0, padx=20, pady=20, columnspan=3)
PL2.grid_remove()
PLstart= Label(PL2,text=' 00:00', background= 'red', width=7)
PLstart.grid(row = 0, column=0)
Prmusic = Progressbar(PL2, orient=HORIZONTAL, mode='determinate', value=0)
Prmusic.grid(row=0, column=1, ipadx=300)
PLend= Label(PL2,text=' 00:00', background= 'red')
PLend.grid(row = 0, column=2)
" ***********************************************Volume Progressbar ****************************"
PL1= Label(root,text=' ', background= 'red')
PL1.grid(row= 0, column=3, padx=20, pady=20, rowspan=3)
PL1.grid_remove()
Pr1 = Progressbar(PL1, orient=VERTICAL, mode='determinate', value=0, length=190)
Pr1.grid(row= 0, column=0)

Pvalue = Label(PL1, text='0%', bg='light grey')
Pvalue.grid(row=0, column=0)
" ************************************************Intro Label*******************"
s = " Developed by Shivam Ojha "
a = 0
text = ' '
L3 = Label(root, text=s , background='sky blue', font=('arial', 30, 'italic bold') )
L3.grid(row=4, column=0,padx=30, pady= 30,columnspan=3)
introLable()
" ********************************Labels***********************************"
L1 = Label(root, text=" Select Music : ", bg='sky blue', font=('arial', 15, 'italic bold') )
L1.grid(row=0, column=0, padx = 20, pady=20)

L2 = Label(root, text=" Please Search Music... ", bg='sky blue', font=('arial', 15, 'italic bold') )
L2.grid(row=2, column=1, padx = 20, pady=20)
" *************************Entry Box***********************************************************"
track = StringVar()
E = Entry(root, textvariable=track, font=('arial', 15, 'italic bold'),width=35)
E.grid(row=0, column=1, padx = 20, pady=20)
" ****************************************Buttons ******************Buttons************************"
"Images****"
isearch = PhotoImage(file='loupe.png')
isearch = isearch.subsample(20,20)
search = Button(root, text='Search ' ,bg='Pink',font=('arial', 14, 'italic bold'), activebackground= 'yellow',
                image=isearch, width=140, compound='right', command=lambda : click('search'))
search.grid(row=0, column=2, padx=20, pady=20)

"Images****"
iplay = PhotoImage(file='play.png')
iplay = iplay.subsample(20,20)
play = Button(root, text='Play Song' ,bg='green',font=('arial', 14, 'italic bold'),
              activebackground= 'yellow', width=140, image=iplay, compound="right",command=lambda : click('play') )
play.grid(row=1, column=0, padx=20, pady=20)

"Images****"
istop = PhotoImage(file='stop.png')
istop = istop.subsample(20,20)
stop = Button(root, text='Stop Song' ,bg='red',font=('arial', 14, 'italic bold'),
              activebackground= 'yellow', width=140, image=istop, compound="right",command=lambda : click('stop'))
stop.grid(row=2, column=0, padx=20, pady=20)

"Images****"
ipause = PhotoImage(file='pause.png')
ipause = ipause.subsample(20,20)
root.pause = Button(root, text='Pause ' ,bg='yellow',font=('arial', 14, 'italic bold'),
                activebackground= 'green', width=150, image=ipause, compound="right",command=lambda : click('pause'))
root.pause.grid(row=1, column=1, padx=20, pady=20)

iresume = PhotoImage(file='resume.png')
iresume = iresume.subsample(20,20)
root.resume = Button(root, text='Resume ' ,bg='yellow',font=('arial', 14, 'italic bold'),
                activebackground= 'green', width=150, image=iresume, compound="right",command=lambda : click('resume'))
root.resume.grid(row=1, column=1, padx=20, pady=20)
root.resume.grid_remove()

"Images****"
vup = PhotoImage(file='Vup.png')
vup = vup.subsample(20,20)
Volumeup = Button(root, text='Volume ' ,bg='grey',font=('arial', 14, 'italic bold'),
                  activebackground= 'green',width=140, image=vup, compound="right",command=lambda : click('vup'))
Volumeup.grid(row=1, column=2, padx=20, pady=20)
"Images****"
vdown = PhotoImage(file='Vdown.png')
vdown = vdown.subsample(20,20)
Volumedown = Button(root, text='Volume ' ,bg='grey',font=('arial', 14, 'italic bold'),
                    activebackground= 'green', width=140, image=vdown, compound='right', command=lambda : click('vdown'))
Volumedown.grid(row=2, column=2, padx=20, pady=20)
"******************************************Mute and Unmute buttons******************"
"Images****"
imute = PhotoImage(file='mute.png')
imute = imute.subsample(30,30)
root.Mute = Button(root, text='Mute ' ,bg='pink',font=('arial', 10, 'italic bold'), activebackground= 'blue',
                   width=80,bd=5, image=imute, compound='right', command=lambda : click('mute'))


iunmute = PhotoImage(file='unmute.png')
iunmute = iunmute.subsample(30,30)
root.Unmute = Button(root, text='Unmute ' ,bg='pink',font=('arial', 10, 'italic bold'),
                    activebackground= 'blue', width=80,bd=5, image=iunmute,
                compound='right', command=lambda : click('unmute'))

mixer.init()
root.mainloop()