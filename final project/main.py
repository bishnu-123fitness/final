import tkinter as tk
import ttkbootstrap as ttk
import customtkinter
import bmictk as b
import workout1 as wa
import rcal as rc
import diett as dt
from tkinter import *
from PIL import Image, ImageTk

root2=None
main_frame=None
def config():
    global main_frame,root2

    
# /// root2 /// 
    root2 = Tk()
    root2.title('Hastag Fitness')
    root2.geometry('550x450')
    root2.minsize(550,450)

    # /// style /// 
    my_style = ttk.Style()
    my_style.configure('success.Outline.TButton', font=("Helvetica", 20))
    my_style.configure('success.TButton', font=("Helvetica", 12))



# widgets 
    main_frame = ttk.Frame(root2, width=530, height=420)
    main_frame.pack(pady=30)
    hastag()

# def bmi():
   
#     root =Toplevel()

#     root.title('BMI Calculator')
# # root.iconbitmap('')
#     root.geometry('500x630')
#     # meter = ImageTk.PhotoImage(Image.open("abmi/meter2.png"))
#     # meter_img = Label(root, image=meter, bd=0)
#     # meter_img.pack(pady=20)

#     customtkinter.set_appearance_mode("dark")
#     customtkinter.set_default_color_theme("dark-blue")

# # function defining 
#     def clear_screen():
#       h_entry.delete(0,END)
#       w_entry.delete(0,END)
#       results.config(text='')

#     def get_bmi():
#     # calculate bmi 
#     # weight_pounds/height_inches^2) * 703 
#       our_height = int(h_entry.get())* int(h_entry.get())
#       out_weight = int(w_entry.get())
#       bmi = (out_weight/our_height)*703
#       bmi_rounded = round(bmi, 1)

#       results.configure(text=f"{str(bmi_rounded)}")


#     # logic 
#       if bmi_rounded < 18.5:
#           results.configure(text=f"{str(bmi_rounded)}\nUnderweight", text_color='#54b1e1')
#       elif bmi_rounded >= 18.5 and bmi_rounded <= 24.9:
#           results.configure(text=f"{str(bmi_rounded)}\nNormal", text_color='#b3d686')
#       elif bmi_rounded >= 25.0 and bmi_rounded <= 29.9:
#           results.configure(text=f"{str(bmi_rounded)}\nOverweight", text_color='#fed429')
#       elif bmi_rounded >= 30.0 and bmi_rounded <= 34.9:
#          results.configure(text=f"{str(bmi_rounded)}\nObese", text_color='#fbaf42')
#       elif bmi_rounded >= 35:
#         results.configure(text=f"{str(bmi_rounded)}\nExtreme Obese", text_color='#f25356')
#     root.mainloop()

# window 
#     root = customtkinter.CTk()

#     root.title('BMI Calculator')
# # root.iconbitmap('')
#     root.geometry('500x630')

# define the image 
    # meter = ImageTk.PhotoImage(Image.open("abmi/meter2.png"))
    # meter_img = Label(root, image=meter, bd=0)
    # meter_img.pack(pady=20)

# defint entry boxes 
#     h_entry = customtkinter.CTkEntry(master=root,
#                                  placeholder_text="Height In Inches",
#                                  width=200,
#                                  height=30,
#                                  border_width=1,
#                                  corner_radius=10)
#     h_entry.pack(pady=20)

#     w_entry = customtkinter.CTkEntry(master=root,
#                                  placeholder_text='Weight In Pounds',
#                                  width=200,
#                                  height=30,
#                                  border_width=1,
#                                  corner_radius=10)
#     w_entry.pack(pady=20)


# # buttons 
#     button_1 = customtkinter.CTkButton(master=root,
#                                    text="Calculate BMI",
#                                    width=190,
#                                    height=40,
#                                    compound='top',
#                                    command=get_bmi)
#     button_1.pack(pady=20)

#     button_2 = customtkinter.CTkButton(master=root,
#                                    text='Clear Screen',
#                                    width=190,
#                                    height=40,
#                                    fg_color="#D35B58",
#                                    hover_color="#C77C78",
#                                    command=clear_screen)
#     button_2.pack(pady=20)



# # result 
#     results = customtkinter.CTkLabel(master=root, 
#                                  text='',
#                                  font=customtkinter.CTkFont(size=30, weight='bold'),)
#     results.pack(pady= 50)



# # run 
#     if(__name__=="__main__"):
#         root.mainloop()
    
    
    

def hastag():
# /// main buttons /// 

    BMI_button = ttk.Button(main_frame, text='BMI',
                        style="success.Outline.TButton",
                          width=40,command=b.config)
    calorie_button = ttk.Button(main_frame,
                            text='CALORIE COUNT',
                            style="success.Outline.TButton",
                             width=40, command=rc.config)
    diet_button = ttk.Button(main_frame,
                            text='DIET PLAN',
                            style="success.Outline.TButton",
                             width=40, command=dt.config)
    workout_button = ttk.Button(main_frame,
                            text='WORKOUT',
                            style="success.Outline.TButton",
                             width=40, command=wa.config)

    back_button = ttk.Button(main_frame,
                         text='<<<',
                         style="success.TButton"
                         )

    # widgets layout 
    BMI_button.pack(padx=10, pady=15)
    calorie_button.pack(padx=10, pady= 15)
    diet_button.pack(padx=10, pady= 15)
    workout_button.pack(padx=10, pady= 15)
    back_button.pack(pady=15)




# # run 
# if(__name__=="__main__"):
#     root2.mainloop()