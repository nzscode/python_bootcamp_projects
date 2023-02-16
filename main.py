from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FCFFE7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    start_timer()
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    # work_sec = WORK_MIN * 60
    work_sec = 5
    # short_break_sec = SHORT_BREAK_MIN * 60
    short_break_sec = 3
    # long_break_sec = LONG_BREAK_MIN * 60
    long_break_sec = 8
    if reps % 2:
        countdown(short_break_sec)
        reps += 1
        print(reps)
    elif reps == 8:
        countdown(long_break_sec)
        reps += 1
        print(reps)
    else:
        countdown(work_sec)
        reps += 1
        print(reps)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
# title_label.pack()
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
# canvas.pack()
canvas.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), command=start_timer)
# start_button.place(x=-50, y=250)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), command=reset_timer)
# reset_button.place(x=185, y=250)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✔", font=(FONT_NAME, 14, "normal"), bg=YELLOW, fg=GREEN)
# complete_label.place(x=50, y=300)
check_marks.grid(row=3, column=1)


window.mainloop()