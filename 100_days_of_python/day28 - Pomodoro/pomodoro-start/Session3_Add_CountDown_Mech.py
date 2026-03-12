# import tkinter
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1 # 1ST REP

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
    # #If it's the 1st/3rd/5th/7th rep:
    # count_down(work_sec)
    # #If it's the 8th rep:
    # count_down(long_break_sec)
    # #If it's 2nd/4th/6th repo:
    # count_down(short_break_sec)
    # # count_down(5)
    # count_down(5 * 60) #for 5min but its in visualize in 300sec
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # "01:35"
    # 300
    # 245 =
    # 245 / 60 = 4 minutes
    # 245 % 60 = "its gives exact remainder in this case that's second."
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # if count_sec == 0:
    if count_sec < 10:
        # count_sec = "00" # python has dynamic typing
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# count_down(5) initial on this line later cut this line and put in below canvas

# def say_something(thing):
#     print("thing")
# window.after(1000, say_something, "Hello" ) # execute a command after a time delay
# def say_something(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# window.after(2000, say_something, 2,4,6)

title_label = Label(text="Timer", fg=GREEN, bg= YELLOW, font=(FONT_NAME,50))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# count_down(5) # and again this count_down cut from here put separate func.

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=1)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()