from tkinter import *
from time import strftime
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import threading
import time


root = Tk()
root.title("Numerical Computing Implementation")  # title of the application
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # getting the screen height and width
root.geometry("%dx%d" % (w * 0.80, h * 0.80))  # setting the Window Size to 80% of the screen size
root.resizable(False, False)


def toggle_fullscreen(event):  # Toggling Full screen ON when F11 is Pressed
    root.attributes("-fullscreen", True)
    return "break"


def end_fullscreen(event):  # Toggling Full screen OFF when Esc is Pressed
    root.attributes("-fullscreen", False)
    return "break"


def on_closing():  # Confirmation to Exit the Program
    if messagebox.askyesnocancel("Confirm Exit ", "Are you sure you want to exit ?"):
        root.destroy()


def resize_image(event):  # Function to resize images according to Screen Resolution
    new_width = event.width
    new_height = event.height
    path = copy_of_image.resize((new_width, new_height))
    photo1 = ImageTk.PhotoImage(path)
    background_label.config(image=photo1)
    background_label.image = photo1  # avoid garbage collection


def new_img():  # Generates Random number for images and returns the path of the image generated

    number = random.randint(1, 44)  # Pick a new number
    path = 'D:/NCproject/Background_Images/' + str(number) + '.png'
    return path


image = Image.open(new_img())
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)

# background_label = Label(root, image=photo)
# background_label.bind('<Configure>', resize_image)
# background_label.grid(row=0, column=0)  # Placement of the image

side_panel = Frame(root, bg="#3498db", width=100, bd=5)
side_panel.grid(row=0, column=0, sticky=S+W)

exit_button = Button(side_panel, text="Exit", padx=10, pady=10, width=15, relief=RAISED, bd=5, command=on_closing)
exit_button.grid(row=1, column=1, sticky="s")

Help = Button(side_panel, text="Help", padx=10, pady=10, width=15, relief=RAISED, bd=5)
Help.grid(row=2, column=1, sticky=S+W)
# Help = Button(side_panel, text="Help", padx=10, pady=15, width=15, relief=RAISED, bd=5, bitmap="question")
# Help.grid(row=2, column=1, sticky=S+W)
#
settings = Button(side_panel, text="Settings", padx=10, pady=10, width=15, relief=RAISED, bd=5)
settings.grid(row=3, column=1, sticky=S+W)
#
# top_frame = Frame(root, height=20)
# top_frame.pack(fill=X, side=TOP)
#
# label = Label(top_frame, text="Welcome To NC Computing ", height=5, bd=5, relief=SUNKEN, font="Times 18 bold italic")
# label.pack(fill=X)
# main_frame = Frame(root)
# main_frame.pack()
#
# chap2 = Button(main_frame, text="Solution(Root) of equations", padx=10, pady=10, width=70, relief=RAISED, bd=5)
# chap2.pack(anchor=CENTER)
# chap2 = Button(main_frame, text="Solution(Root) of equations", padx=10, pady=10, width=70, relief=RAISED, bd=5)
# chap2.pack(anchor=CENTER)
# chap2 = Button(main_frame, text="Solution(Root) of equations", padx=10, pady=10, width=70, relief=RAISED, bd=5)
# chap2.pack(anchor=CENTER)
# chap2 = Button(main_frame, text="Solution(Root) of equations", padx=10, pady=10, width=70, relief=RAISED, bd=5)
# chap2.pack(anchor=CENTER)
# chap2 = Button(main_frame, text="Solution(Root) of equations", padx=10, pady=10, width=70, relief=RAISED, bd=5)
# chap2.pack(anchor=CENTER)
# chap2 = Button(main_frame, text="Solution(Root) of equations", padx=10, pady=10, width=70, relief=RAISED, bd=5)
# chap2.pack(anchor=CENTER)
#
#
# root.bind("<F11>", toggle_fullscreen)
# root.bind("<Escape>", end_fullscreen)

# root.protocol("WM_DELETE_WINDOW", on_closing)  # Modifying close button function

root.mainloop()
exit()
from tkinter import *
from time import strftime
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Numerical Computing Implementation")  # title of the application
w, h = root.winfo_screenwidth(), root.winfo_screenheight()  # getting the screen height and width
root.geometry("%dx%d" % (w * 0.75, h * 0.750))  # setting the Window Size to 80% of the screen size


def callback():
    lbl = Label(root, text=e.get()).pack()


def click():
    e.delete(0, END)


def clear_search(event):        # Clearing the entry box upon clicking on it
    e.delete(0, END)


def on_enter(e):            # hover on button color change
    b['background'] = '#3498db'
    b.config(relief='raised')


def on_leave(e):            # leaving hover on button getting normal
    b['background'] = 'SystemButtonFace'
    b.config(relief='flat')


b = Button(root, text="Submit", width=50, height=5,  font='Rockwell', relief=RIDGE, bd=10, activebackground="green", command=callback)
b.place(relx=0.4, rely=0.5)
# b1 = Button(root, text="Submit", width=50, bg="#C8F9C4", height=5, relief='raised', font='Rockwell', bd=10, activebackground="green", command=callback)
# b1.place(relx=0.5, rely=0.6)

e = Entry(root, width=50,)
e.pack()
e.insert(0, "Enter an Expression")
text = e.get()
e.bind("<FocusIn>", clear_search)

b.bind("<Enter>", on_enter)
b.bind("<Leave>", on_leave)
#!/usr/bin/env python3

"""
ZetCode Tkinter tutorial

In this script, we use the grid
manager to create a more complicated Windows
layout.

Author: Jan Bodnar
Last modified: April 2019
Website: www.zetcode.com
"""

from tkinter import Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Windows")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="Windows")
        lbl.grid(sticky=W, pady=4, padx=5)

        area = Text(self)
        area.grid(row=1, column=0, columnspan=2, rowspan=4,
            padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="Activate")
        abtn.grid(row=1, column=3)

        cbtn = Button(self, text="Close")
        cbtn.grid(row=2, column=3, pady=4)

        hbtn = Button(self, text="Help")
        hbtn.grid(row=5, column=0, padx=5)

        obtn = Button(self, text="OK")
        obtn.grid(row=5, column=3)


def main():

    root = Tk()
    root.geometry("350x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
# root.mainloop()

