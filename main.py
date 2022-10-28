from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
from PIL import ImageTk, Image
import os


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("musicPlayer2.0")
window.geometry("577x730")
window.configure(bg="#4a532b")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=730,
    width=577,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

mixer.init()


def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        ##       print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])


entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    289.0, 345.0,
    image=entry0_img)

canvas.create_rectangle(
    40, 552, 40 + 490, 552 + 90,
    fill="#edf2fa",
    width="8",
    outline="#317cf5")

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=play_song,
    relief="flat")

b0.place(
    x=187, y=562,
    width=55,
    height=70)

img1 = PhotoImage(file=f"img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=mixer.music.pause,
    relief="flat")

b1.place(
    x=276, y=562,
    width=51,
    height=70)

img2 = PhotoImage(file=f"img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=mixer.music.unpause,
    relief="flat")

b2.place(
    x=361, y=562,
    width=55,
    height=64)

img3 = PhotoImage(file=f"img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=open_folder,
    relief="flat")

b3.place(
    x=471, y=571,
    width=42,
    height=48)

img4 = PhotoImage(file=f"img4.png")
b4 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=mixer.music.stop,
    relief="flat")

b4.place(
    x=105, y=565,
    width=48,
    height=64)

# label
music = Label(window, text="", font=("arial", 8),fg="black")
music.place(x=200, y=10, anchor="center")

# logo
Logo = ImageTk.PhotoImage(file="img6.jpg")
Label(window, image=Logo).place(x=30, y=70, width=300, height=450)

# music
#Menu = PhotoImage(file="img5.png")
#Label(window, image=Menu).place(x=250, y=70, width=300, height=450)

music_frame = Frame(window, bd=2, relief=RIDGE)
music_frame.place(x=330, y=70, width=210, height=450)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, bg="#333333", fg="grey", selectbackground="lightblue",
                   cursor="hand2", bd=0,
                   yscrollcommand=scroll.set)

scroll.config(command=playlist.yview_scroll)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

window.resizable(False, False)
window.mainloop()
