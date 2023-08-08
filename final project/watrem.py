from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification
import time
from datetime import datetime, timedelta

# Global variables
reminder_interval = 60
remaining_time = timedelta(seconds=0)
start_time = datetime.now()

# defining functions
def clicker():
    global remaining_time, start_time
    remaining_time = timedelta(minutes=reminder_interval)
    start_time = datetime.now()
    update_timer_label()
    root.after(reminder_interval * 60 * 1000, show_water_reminder)  # Convert minutes to milliseconds and start countdown

def show_water_reminder():
    global remaining_time, start_time
    toast.show_toast()
    remaining_time = timedelta(minutes=reminder_interval)
    start_time = datetime.now()
    update_timer_label()
    root.after(reminder_interval * 60 * 1000, show_water_reminder)  # Convert minutes to milliseconds and repeat the reminder

def set_reminder_interval():
    global reminder_interval
    try:
        interval = int(interval_entry.get())
        if interval <= 0:
            raise ValueError("Interval must be a positive integer.")
        reminder_interval = interval
        interval_label.config(text=f"Reminder Interval: {reminder_interval} minutes")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def update_timer_label():
    global remaining_time, start_time
    current_time = datetime.now()
    elapsed_time = current_time - start_time
    remaining_time = timedelta(seconds=max(0, reminder_interval * 60 - elapsed_time.total_seconds()))
    timer_label.config(text=f"Next Reminder in: {str(remaining_time).split('.', 2)[0]}")

    if remaining_time.total_seconds() <= 0:
        toast.show_toast()
        remaining_time = timedelta(minutes=reminder_interval)
        start_time = datetime.now()

    root.after(1000, update_timer_label)  # Update the timer label every second (1000 milliseconds)

# window
root = ttk.Window(themename="superhero")
root.title('Water Reminder')
root.geometry('400x250')

# Widget
toast = ToastNotification(title='Stay Hydrated!',
                          message="Remember to take a break and drink some water.",
                          duration=3000,  # Display the toast notification for 3 seconds
                          alert=True,
                          position=('sw'))

my_button = ttk.Button(root, text="Start Reminder", command=clicker)
my_button.pack(pady=10)

interval_frame = ttk.Frame(root)
interval_frame.pack(pady=10)

interval_label = ttk.Label(interval_frame, text="Reminder Interval: 60 minutes")
interval_label.pack(side=LEFT)

interval_entry = ttk.Entry(interval_frame, width=5)
interval_entry.pack(side=LEFT)

set_interval_button = ttk.Button(interval_frame, text="Set Interval", command=set_reminder_interval)
set_interval_button.pack(side=LEFT)

# Timer label to display the remaining time until the next reminder
timer_label = ttk.Label(root, text="Next Reminder in: ", font=("Arial", 12))
timer_label.pack(pady=20)

# run
root.mainloop()
