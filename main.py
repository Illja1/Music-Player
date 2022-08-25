from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os
from PIL import Image, ImageTk
from pytube import Playlist

root = Tk()
root.title('Music player')
root.geometry("920x670")
root.configure(bg="#0f1a2b")
mixer.init()

#Create func for adding Music
def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith('.mp3'):
                Playlist.insert(END, song)

#Create func for play Music
def Play_Music():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


#Make icon and logo

Icon_Image = PhotoImage(file="photo_1/play_button.png")
root.iconphoto(False, Icon_Image)


#Create music play btn
Button_Play = PhotoImage(file='photo_1/play_button.png')
Button(root, image=Button_Play, bg="#0f1a2b", bd=0,command=Play_Music).place(x=115, y=400)


#Create music stop bnt
Button_Stop = PhotoImage(file='photo_1/stop_button.png')
Button(root, image=Button_Stop,bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=10, y=500)


#Create resume btn
Button_Resume = PhotoImage(file="photo_1/resume_button.png")
Button(root, image=Button_Resume, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)


#Create pause btn
Button_Pause = PhotoImage(file="photo_1/pause_button.png")
Button(root, image=Button_Pause, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=220, y=500)


Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)

Button(root, text="Add Music", width=15, height=2, font=("times new roman", 12, "bold"), fg="Black", bg="#21b3de",
       command=Add_Music).place(x=330, y=300)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()
