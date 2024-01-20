import math
from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.3
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.2
reps = 0
checkMarks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global checkMarks
    reps += 1
    global work_count
    if reps % 8 == 0:
        label.config(text="Long Break", bg=RED)
        window.config(bg=RED)
        check_mark_row.config(bg=RED)
        canvas.config(bg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        label.config(text="Short Break",bg=YELLOW)
        window.config(bg=YELLOW)
        check_mark_row.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        count_down(SHORT_BREAK_MIN*60)
    else:
        label.config(text="Work Time", bg=GREEN)
        window.config(bg=GREEN)
        check_mark_row.config(bg=GREEN, fg=RED)
        canvas.config(bg=GREEN)
        count_down(WORK_MIN*60)
        checkMarks = ''.join("✔" for mark in checkMarks)
        checkMarks += "🔘"
        check_mark_row.config(text=checkMarks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)
label = Label(text="Timer",font=(FONT_NAME, 40, "bold"), bg= PINK, fg=GREEN)
label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224,bg=PINK, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=2, column=2)

check_mark_row = Label(text=checkMarks, fg=GREEN, bg=PINK)
check_mark_row.config(pady=10, padx=20)
check_mark_row.grid(row=3, column=1)

window.mainloop()
