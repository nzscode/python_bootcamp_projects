from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#FCFFE7")
canvas = Canvas(width=200, height=230, bg="#FCFFE7", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 115, image=tomato_img)
canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.pack()



window.mainloop()