from tkinter import Tk, StringVar, Label, Entry, Button
from pytube import YouTube

root = Tk()
root.geometry('500x250+700+300')
root.resizable(0, 0)
root.title("YouTube Video Downloader")

link = StringVar()
Label(root, text='Link:', font='arial 15 bold').place(x=220, y=60)
Label(root, text='YouTube Video Downloader',
      font='arial 15 bold').place(x=80, y=10)
Entry(root, width=70, textvariable=link).place(x=32, y=90)


def download_vid():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Fertig!', font='arial 15').place(x=170, y=210)


Button(root, text='DOWNLOAD VIDEO', font='arial 15 bold',
       bg='red', padx=2, command=download_vid).place(x=140, y=150)

root.mainloop()
