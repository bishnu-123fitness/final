from tkinter import *
import tkinter.messagebox as messagebox
import random
import ttkbootstrap as ttk
def config():
    # Function to show random upper body workout recommendations
    def show_random_upper_body_workouts():
        upper_body_workouts = [
            {"exercise": "Push-ups", "sets": 3, "reps": 10},
            {"exercise": "Dumbbell Shoulder Press", "sets": 3, "reps": 8},
            {"exercise": "Bent-over Rows", "sets": 3, "reps": 10},
            {"exercise": "Bicep Curls", "sets": 3, "reps": 12},
            {"exercise": "Pull-ups", "sets": 3, "reps": 8},
            {"exercise": "Overhead Press", "sets": 3, "reps": 10},
            {"exercise": "Dumbbell Flyes", "sets": 3, "reps": 12},
            {"exercise": "Tricep Dips", "sets": 3, "reps": 12},
            {"exercise": "Chest Dips", "sets": 3, "reps": 10},
        ]
        random.shuffle(upper_body_workouts)
        recommended_workouts = upper_body_workouts[:5]
        show_workout_window("Random Upper Body Workouts", recommended_workouts)
    
    # Function to show random lower body workout recommendations
    def show_random_lower_body_workouts():
        lower_body_workouts = [
            {"exercise": "Squats", "sets": 4, "reps": 10},
            {"exercise": "Romanian Deadlifts", "sets": 3, "reps": 8},
            {"exercise": "Leg Press", "sets": 3, "reps": 12},
            {"exercise": "Leg Curls", "sets": 3, "reps": 12},
            {"exercise": "Calf Raises", "sets": 3, "reps": 15},
            {"exercise": "Lunges", "sets": 3, "reps": 10},
            {"exercise": "Glute Bridges", "sets": 3, "reps": 12},
            {"exercise": "Hamstring Curls", "sets": 3, "reps": 10},
            {"exercise": "Step-ups", "sets": 3, "reps": 10},
        ]
        random.shuffle(lower_body_workouts)
        recommended_workouts = lower_body_workouts[:5]
        show_workout_window("Random Lower Body Workouts", recommended_workouts)
    
    # Function to create a new window with the selected workouts
    def show_workout_window(title, recommended_workouts):
        workout_win = Toplevel(win)
        workout_win.title(title)
        workout_win.geometry('600x550')
    
        # Apply the same styling to the new window
        workout_win_style = ttk.Style()
        workout_win_style.configure('success.TButton', font=("Helvetica", 12))
    
        workout_label = Label(workout_win, text="Today's Recommended Workouts:", font=("Helvetica", 14, "bold"))
        workout_label.pack(pady=10)
    
        for workout in recommended_workouts:
            frame = Frame(workout_win, highlightbackground="green",highlightthickness=2)
            frame.pack(padx=20, pady=10, fill="both")
    
            exercise_label = Label(frame,text=f"Exercise: {workout['exercise']}\nSets: {workout['sets']}\nReps: {workout['reps']}", font=("Helvetica", 12))
            exercise_label.pack()
    
    # Window
    win = ttk.Window(themename='lumen')
    win.geometry('550x450')
    
    # Style
    my_style = ttk.Style()
    my_style.configure('success.Outline.TButton', font=("Helvetica", 20))
    my_style.configure('success.TButton', font=("Helvetica", 12))
    
    # Widgets
    upper_button = ttk.Button(win,
                              text='UPPER',
                              style="success.Outline.TButton",
                              width=35,
                              command=show_random_upper_body_workouts)
    
    lower_button = ttk.Button(win,
                              text='LOWER',
                              style="success.Outline.TButton",
                              width=35,
                              command=show_random_lower_body_workouts)
    
    back2_button = ttk.Button(win,
                              text='<<<',
                              style="success.Outline.TButton")
    
    # Layouts
    upper_button.pack(padx=20, pady=(90, 30))
    lower_button.pack(padx=20, pady=(30, 70))
    back2_button.pack(padx=60, pady=30)
    
    # Run
    win.mainloop()
    