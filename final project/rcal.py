import tkinter as tk
from tkinter import messagebox


def config():

    def on_validate_input(value):
        if value.strip() == "":
            return True
    
        try:
            float(value)
            return True
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter integers only.")
            return False
    
    
    def add():
        try:
            total = 0
            for entry, calorie in entries.items():
                try:
                    value = int(entry.get())
    
                    total += value * calorie
                except ValueError:
                    pass
                
            result_label.config(text=f"Total calorie = {total:.2f}")
        except ValueError:
            result_label.config(text="Please enter valid numeric values")
    
    
    root = tk.Tk()
    root.title('Calorie Calculator')
    root.geometry("400x400")
    root.resizable(1, 1)
    
    food_calories = {
        "Boiled Egg (per egg)": 155,
        "Salmon (per gram)": 2.08,
        "Chicken Breast (per gram)": 1.65,
        "Yogurt (per gram)": 0.59,
        "Tuna (per gram)": 1.32,
        "Shrimp (per gram)": 0.99,
        "Soybeans (per gram)": 4.46,
        "Cottage Cheese (per gram)": 0.98,
        "Beans (per gram)": 3.47,
        "Peanuts (per gram)": 5.67,
        "Buckwheat (per gram)": 3.43,
        "Milk (per cup)": 42,
        "Almond (per gram)": 5.79,
        "Brown Rice (per gram)": 1.11
    }
    
    entries = {}
    
    row = 1
    for food, calorie in food_calories.items():
        label = tk.Label(root, text=food)
        label.grid(row=row, column=1)
    
        vcmd = (root.register(on_validate_input), '%P')
        entry = tk.Entry(root, validate='key', validatecommand=vcmd)
        entry.grid(row=row, column=2)
        entries[entry] = calorie
        row += 1
    
    calculate = tk.Button(root, text='Calculate', command=add)
    calculate.grid(row=row, column=2)
    
    result_label = tk.Label(root, text="", font=("Helvetica", 12))
    result_label.grid(row=row + 1, column=2)
    
    root.mainloop()