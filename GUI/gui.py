import tkinter as tk

app = tk.Tk()
app.geometry("800x450")
app.configure(bg="white")
app.title("Kitchen Management")

# Create left panel with three buttons
left_panel = tk.Frame(master=app, width=200, bg="white")
left_panel.pack(side="left", fill="both")

table_1_button = tk.Button(master=left_panel, text="Table-1", font=("Helvetica", 18),bg="white", fg="black")
table_1_button.pack(side="top", pady=20)

table_2_button = tk.Button(master=left_panel, text="Table-2", font=("Helvetica", 18),bg="white", fg="black")
table_2_button.pack(side="top", pady=20)

table_3_button = tk.Button(master=left_panel, text="Table-3", font=("Helvetica", 18),bg="white", fg="black")
table_3_button.pack(side="top", pady=20)

table_4_button = tk.Button(master=left_panel, text="Table-4", font=("Helvetica", 18),bg="white", fg="black")
table_4_button.pack(side="top", pady=20)

table_5_button = tk.Button(master=left_panel, text="Table-5", font=("Helvetica", 18),bg="white", fg="black")
table_5_button.pack(side="top", pady=20)

# Create dropdown menu on the right side
def edit_menu():
    print("Edit Menu")

def orders_completed():
    print("Orders Completed")

def orders_pending():
    print("Orders Pending")

menu = tk.Menu(app, tearoff=0)

edit_button = tk.Menubutton(master=app, text="EDIT", font=("Helvetica", 18), bg="white", fg="black")
edit_button.pack(side="right", pady=20, padx=20)

edit_button.menu = tk.Menu(edit_button, tearoff=0)
edit_button.menu.add_cascade(label="Edit Menu", command=edit_menu)
edit_button.menu.add_cascade(label="Orders Completed", command=orders_completed)
edit_button.menu.add_cascade(label="Orders Pending", command=orders_pending)
edit_button["menu"] = edit_button.menu

app.mainloop()
