import math
from tkinter import *
import time
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
def start_timer():
    count_down(300)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    cound_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{cound_seconds}")
    if count > 0:
        window.after(1000, count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)
window.after(1000,)
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

check_mark_row = Label(text="✔ ✔ ✔ ✔ ✔", fg=GREEN, bg=PINK)
check_mark_row.config(pady=10, padx=20)
check_mark_row.grid(row=3, column=1)

window.mainloop()
