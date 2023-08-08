from tkinter import Tk 
from tkinter import Label
import time
import sys

# creating window 
master = Tk()
master.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)


# widgets
clock = Label(master, font=('Arial', 90), bg='black', fg='white')
clock.pack()

get_time()

# run 
master.mainloop()