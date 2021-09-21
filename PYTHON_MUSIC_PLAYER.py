import pygame
from pygame import mixer
from tkinter import *
import os


def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing THE MUSICCCCCCCCCCCCCCCCCCC")
    mixer.music.play()


def pausesong():
    songstatus.set("Pausinggggggggggggggggggggggg")
    mixer.music.pause()


root = Tk()
root.title('SPOTIFYTAP')

mixer.init()
songstatus = StringVar()
songstatus.set("LET THE MUSIC BE THERE")

# playlist---------------

playlist = Listbox(root, selectmode=SINGLE, bg="green",
                   fg="white", font=('arial', 15), width=100)
playlist.grid(columnspan=10)

os.chdir(r'C:\Users\anubh\OneDrive\Desktop\MUSIC')
songs = os.listdir()
for s in songs:
    playlist.insert(END, s)

playbtn = Button(root, text="play", command=playsong)
playbtn.config(font=('arial', 20), bg="green",
               fg="white", padx=18, pady=17)
playbtn.grid(row=1, column=0)

pausebtn = Button(root, text="Pause", command=pausesong)
pausebtn.config(font=('arial', 20), bg="green",
                fg="white", padx=18, pady=17)
pausebtn.grid(row=1, column=1)


mainloop()
