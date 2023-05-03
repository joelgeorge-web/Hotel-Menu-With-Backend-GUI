import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x450")
app.title("Kitchen Management")

def button_function():
    print("Menu Edited")
    window1 = ctk.CTkToplevel(app)
    window1.geometry("800x450")
    window1.title("Edit Functions")
    button = ctk.CTkButton(master=app, text="Edit Menu", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    app.mainloop()


    
button = ctk.CTkButton(master=app, text="Edit", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()












