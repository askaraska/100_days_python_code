# import tkinter
from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# window = tkinter.Tk() # creating the window
window = Tk() # creating the window
window.title("My first GUI window")
window.minsize(500,300)
# window.config(padx=20, pady=20) # padding entire window
window.config(padx=100, pady=200)


#label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=0,y=0) # top left corner based on x,y axis
# my_label.place(x=100,y=100)
my_label.grid(row=0, column=0) # based on grid row/column placed the label
my_label.config(padx=50, pady=50)

# my_label.pack()

#button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

#new button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#entry
input = Entry(width=10) # entry give a input
print(input.get()) # entry - get() returns the string
input.grid(row=2, column=3)



window.mainloop() # keep window on , and its placed on very end