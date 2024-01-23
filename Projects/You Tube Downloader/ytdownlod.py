"Python YouTube Downloader with Pytube"

from tkinter import *
from pytube import YouTube

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)





root = Tk()
root.geometry('500x300')
root.resizable(False, False)
root.wm_iconbitmap('y.ico')
root.title("My youtube video downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold', fg='red').pack()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)

link = StringVar()
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2,
       command=Downloader).place(x=180, y=150)

root.mainloop()