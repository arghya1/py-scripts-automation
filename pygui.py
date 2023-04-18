#!/usr/bin/python3

# Modern GUI python app
# Install tkinter using pip install 

import tkinter as tk
from tkinter import filedialog
 
r = tk.Tk()

# Set title
r.title("My awesome gui app")

# Set size
r.geometry("400x400")

# Create a label
label = tk.Label(r, text="Hello awesome human!")
label.place(x=10, y=10)

# Create a Inputbox
value = tk.StringVar()
inputbox = tk.Entry(r, textvariable=value)
inputbox.place(x=10, y=50)

# Create a Button
button = tk.Button(r, text="Take over the world")
button.place(x=10, y=100)

# Create Checkboxes
opt1 =tk.IntVar()
check = tk.Checkbutton(r, text="Awesome option", variable=opt1)
check.place(x=10, y=150)

# Import Image
img = tk.PhotoImage(file="Wifi.png")
image = tk.Label(r, image=img)
image.place(x=10,y=200)

# File Dialog
filedialog.askopenfilename(parent= r)

# run the app
r.mainloop()















