from tkinter import *
import random

# Weight Gain Foods
gain_foods = [
    {
        "name": "Avocado",
        "info": "Avocado is rich in healthy fats, which can help with weight gain.",
        "calories": 160
    },
     {
        "name": "Peanut Butter",
        "info": "Peanut butter is high in calories and protein, making it great for weight gain.",
        "calories": 190
    },
    {
        "name": "Nuts and Seeds",
        "info": "Nuts and seeds are packed with healthy fats and protein for weight gain.",
        "calories": 180
    },
    {
        "name": "Cheese",
        "info": "Cheese is calorie-dense and contains protein and calcium.",
        "calories": 110
    },
    {
        "name": "Whole Milk",
        "info": "Whole milk is rich in calories and fats, promoting weight gain.",
        "calories": 150
    },
    {
        "name": "Olive Oil",
        "info": "Olive oil is high in healthy fats and calories, aiding in weight gain.",
        "calories": 120
    },
    {
        "name": "Granola",
        "info": "Granola is calorie-dense and contains nuts and dried fruits for weight gain.",
        "calories": 120
    },
    {
        "name": "Potatoes",
        "info": "Potatoes are a good source of carbohydrates for weight gain.",
        "calories": 160
    },
    {
        "name": "Brown Rice",
        "info": "Brown rice is a healthy carb source with moderate calories.",
        "calories": 215
    },
    {
        "name": "Bananas",
        "info": "Bananas are rich in calories, carbs, and nutrients for weight gain.",
        "calories": 105
    }
    
]

# Weight Loss Foods
loss_foods = [
    {
        "name": "Green Leafy Vegetables",
        "info": "Green leafy vegetables are low in calories and high in nutrients, aiding in weight loss.",
        "calories": 25
    },
    {
        "name": "Lean Proteins",
        "info": "Lean proteins can boost metabolism and promote weight loss.",
        "calories": 120
    },
    {
        "name": "Lean Proteins",
        "info": "Lean proteins can boost metabolism and promote weight loss.",
        "calories": 120
    },
    {
        "name": "Whole Grains",
        "info": "Whole grains provide fiber and nutrients, supporting weight loss efforts.",
        "calories": 150
    },
    {
        "name": "Berries",
        "info": "Berries are low-calorie and high in antioxidants, beneficial for weight loss.",
        "calories": 70
    },
    {
        "name": "Greek Yogurt",
        "info": "Greek yogurt is high in protein and can help control appetite during weight loss.",
        "calories": 100
    },
    {
        "name": "Cucumber",
        "info": "Cucumber is low in calories and a good hydrating food for weight loss.",
        "calories": 16
    },
    {
        "name": "Tomato",
        "info": "Tomatoes are low in calories and rich in vitamins, aiding in weight loss.",
        "calories": 25
    },
    {
        "name": "Eggs",
        "info": "Eggs are protein-rich and can help you feel full, supporting weight loss.",
        "calories": 78
    },
    
]

current_loss_food_index = -1
loss_window = None

def show_next_loss_food():
    global current_loss_food_index
    current_loss_food_index = (current_loss_food_index + 1) % len(loss_foods)
    food_item = loss_foods[current_loss_food_index]
    food_label.config(text=f"{food_item['name']} - {food_item['info']} \nCalories: {food_item['calories']}")

def weight_loss():
    global current_loss_food_index
    current_loss_food_index = -1

    # Close the main window
    window.destroy()

    # Create a new window for displaying the weight loss food item
    global loss_window
    loss_window = Tk()
    loss_window.title("Weight Loss Food")
    loss_window.geometry("400x200")

    # Display the food item in the new window
    food_item = loss_foods[0]
    global food_label
    food_label = Label(loss_window, text=f"{food_item['name']} - {food_item['info']} \nCalories: {food_item['calories']}", font=("Arial", 12))
    food_label.pack()

    next_button = Button(loss_window, text="Next", command=show_next_loss_food)
    next_button.pack()

    loss_window.mainloop()

current_gain_food_index = -1
gain_window = None

def show_next_gain_food():
    global current_gain_food_index
    current_gain_food_index = (current_gain_food_index + 1) % len(gain_foods)
    food_item = gain_foods[current_gain_food_index]
    food_label.config(text=f"{food_item['name']} - {food_item['info']} \nCalories: {food_item['calories']}")

def weight_gain():
    global current_gain_food_index
    current_gain_food_index = -1

    # Close the main window
    window.destroy()

    # Create a new window for displaying the weight gain food item
    global gain_window
    gain_window = Tk()
    gain_window.title("Weight Gain Food")
    gain_window.geometry("400x200")

    # Display the food item in the new window
    food_item = gain_foods[0]
    global food_label
    food_label = Label(gain_window, text=f"{food_item['name']} - {food_item['info']} \nCalories: {food_item['calories']}", font=("Arial", 12))
    food_label.pack()

    next_button = Button(gain_window, text="Next", command=show_next_gain_food)
    next_button.pack()

    gain_window.mainloop()

window = Tk()
window.title("Weight Management")
window.geometry("300x200")
window.resizable(1, 1)

gain_button = Button(window, text='Weight Gain', command=weight_gain)
gain_button.pack()

loss_button = Button(window, text="Weight Loss", command=weight_loss)
loss_button.pack()

window.mainloop()
