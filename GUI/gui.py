import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark

app = ctk.CTk()
app.geometry("800x450")
app.title("Kitchen Management")

# Create left panel with three buttons
left_panel = ctk.CTkFrame(master=app, width=200, bg_color="dark blue")
left_panel.pack(side="left", fill="both")

table_1_button = ctk.CTkButton(master=left_panel, text="Table-1", font=("Helvetica", 18),fg_color="Blue")
table_1_button.pack(side="top", pady=20)

table_2_button = ctk.CTkButton(master=left_panel, text="Table-2", font=("Helvetica", 18), fg_color="Blue")
table_2_button.pack(side="top", pady=20)

table_3_button = ctk.CTkButton(master=left_panel, text="Table-3", font=("Helvetica", 18), fg_color="Blue")
table_3_button.pack(side="top", pady=20)

# Create edit button on the right side
def button_function():
    print("Menu Edited")
    window1 = ctk.CTkToplevel(app)
    window1.geometry("800x450")
    window1.title("Edit Functions")
    window1.lift() # Bring the window to the front
    app.update() # Update the app to bring the window to the front
    edit_button = ctk.CTkButton(master=window1, text="EDIT", font=("Helvetica", 18), bg_color="blue", fg_color="Blue")
    edit_button.pack(side="top", pady=20)

edit_button = ctk.CTkButton(master=app, text="EDIT", font=("Helvetica", 18), bg_color="blue", fg_color="Blue", command=button_function)
edit_button.pack(side="right", pady=20, padx=20)

app.mainloop()