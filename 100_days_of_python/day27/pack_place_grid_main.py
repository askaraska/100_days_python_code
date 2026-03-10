# import tkinter
from tkinter import *

# window = tkinter.Tk() # creating the window
window = Tk() # creating the window

window.title("My first GUI window")
window.minsize(500,300)

#label

# my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left") # pack our label onto the screen.
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

#button

def button_clicked():
    print("I got clicked Button")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()


#entry

# input = Entry() # entry give a input
input = Entry(width=10) # entry give a input
input.pack()
print(input.get()) # entry - get() returns the string

window.mainloop() # keep window on , and its placed on very end