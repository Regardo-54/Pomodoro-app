import math
from tkinter import *

from PIL import Image, ImageTk

FONT_NAME = "COURIER"
YELLOW = "#f7f5dd"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"

reps = 0
timer = None


def reset_timer():
    global reps, CHECK_MARK,timer
    reps = 0
    CHECK_MARK = "✔"
    top_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        top_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        global CHECK_MARK
        if reps > 2:
            CHECK_MARK += "✔"
        tick_label.config(text=CHECK_MARK)
        if reps % 8 == 0:
            top_label.config(text="Break", fg=RED)
            count_down(long_break_sec)
        else:
            top_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)


def count_down(time):
    minute = math.floor(time / 60)
    second = time % 60

    if second < 10:
        second = f"0{second}"
    if minute < 10:
        minute = f"0{minute}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time - 1)
    else:
        start_timer()


window = Tk()
window.title("Pamodoro")
window.config(padx=100, pady=60, bg=YELLOW)

image_1 = Image.open("tomato.png")
resized_img = image_1.resize((260, 284))
T_image = ImageTk.PhotoImage(resized_img)

top_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
top_label.grid(row=0, column=1)
top_label.config(pady=10)

canvas = Canvas(width=284, height=260, bg=YELLOW, highlightthickness=0)
canvas.create_image(142, 120, image=T_image)
timer_text = canvas.create_text(142, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg="White", fg="Black", font=(FONT_NAME, 10), command=start_timer)
start_button.grid(row=2, column=0)

tick_label = Label(text="", font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
tick_label.grid(row=3, column=1)

reset_button = Button(text="Reset", bg="White", fg="Black", font=(FONT_NAME, 10), command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
