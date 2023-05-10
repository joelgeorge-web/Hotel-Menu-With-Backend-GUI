from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import threading
import webbrowser
import logging
from tkinter import ttk
import scripts


#Connection to mysql database running on localhost

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db"
    )

#connecting to the database from flask app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/db'
db = SQLAlchemy(app)

#creating a messagebox to display the message

def showMessage(message, type='info', timeout=2500):
    import tkinter as tk
    from tkinter import messagebox as msgb

    root = tk.Tk()
    root.withdraw()
    try:
        root.after(timeout, root.destroy)
        if type == 'info':
            msgb.showinfo('Info', message, master=root)
        elif type == 'warning':
            msgb.showwarning('Warning', message, master=root)
        elif type == 'error':
            msgb.showerror('Error', message, master=root)
    except:
        pass

#create a gui for the tab part(queuing system)

def tab():
    app1 = tk.Tk()
    width= app1.winfo_screenwidth()               
    height= app1.winfo_screenheight()
    app_width = width // 2
    app_height = height
    app_geometry = f"{app_width}x{app_height}+0+0"
    app1.geometry(app_geometry)
    app1.configure(bg="white")
    app1.title("Tab")

    # Create call any robot Button
    bot1 = tk.Button(master=app1, text="CALL ANY ROBOT", font=("Helvetica", 18), bg="white", fg="black")
    bot1.pack(pady=(50,50), padx=20)

    # Create a labels for the taking user details and create entry boxes for the same
    heading1_label = tk.Label(master=app1, text="ENTER YOUR NAME", font=("Helvetica", 18), bg="white", fg="black")
    heading1_label.pack(pady=(20,1))
    bot2_entry = tk.Entry(master=app1, font=("Helvetica", 20), width=10,bg="white")
    bot2_entry.pack(pady=(1,5), padx=20)
    heading2_label = tk.Label(master=app1, text="ENTER YOUR PHONE NUMBER", font=("Helvetica", 18), bg="white", fg="black")
    heading2_label.pack(pady=(20,1))
    bot3_entry = tk.Entry(master=app1, font=("Helvetica", 20), width=10,bg="white")
    bot3_entry.pack(pady=(1,5), padx=20)
    heading3_label = tk.Label(master=app1, text="ENTER NUMBER OF GUESTS", font=("Helvetica", 18), bg="white", fg="black")
    heading3_label.pack(pady=(20,1))
    bot4_entry = tk.Entry(master=app1, font=("Helvetica", 20), width=10,bg="white")
    bot4_entry.pack(pady=(1,5), padx=20)
    logging.basicConfig(level=logging.DEBUG)

#save function to save the data in the database when the save button is clicked

    def save_data():
        numg1 = bot2_entry.get()
        numg2 = int(bot3_entry.get())
        numg3 = int(bot4_entry.get())
        cursor1 = mydb.cursor()
        sql = "INSERT INTO guest VALUES (%s, %s, %s)"
        values = (numg1, numg2, numg3)
        cursor1.execute(sql, values)
        mydb.commit()
        print(cursor1.rowcount, "record inserted.")
        print(values)
        showMessage("Data saved successfully!", timeout=500)

# Create a save button to save the data in the database

    bot2 = tk.Button(master=app1, text="SAVE", font=("Helvetica", 18), bg="white", fg="black", command=save_data)
    bot2.pack(pady=10, padx=20)
#calling the gui
    app1.mainloop()

#creating a gui for the kitchen management system

def gui():

    # Create a function to display the table 1 data

    def iddd():
        sql1 = "select * from selected ORDER BY id DESC LIMIT 1"
        mycursor1 = mydb.cursor()
        mycursor1.execute(sql1)
        a =  mycursor1.fetchone()[0]
        return a


    def table1():
        
        idd = iddd()
        sql2 = "SELECT * FROM selected WHERE id = %s"
        mycursor = mydb.cursor()
        mycursor.execute(sql2, (idd,))
        result = mycursor.fetchone()
        
        data2 = result[1]
        data3 = result[2]
        data4 = result[3]
        data5 = result[4]
        data6 = result[5]
        data7 = result[6]
        messagebox.showinfo("ORDER-1",f"CHICKEN AND EGG: {data2}\n CHICKEN TENDER: {data3}\n CHICKEN SALAD: {data4}\n PUMPKIN SOUP: {data5}\n SALAD: {data6}\n PIZZA: {data7}\n")
        mycursor.close()

    def table2():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM selected WHERE id = 11")
        result = mycursor.fetchone()
        
        data2 = result[1]
        data3 = result[2]
        data4 = result[3]
        data5 = result[4]
        data6 = result[5]
        data7 = result[6]
        messagebox.showinfo("ORDER-2",f"CHICKEN AND EGG: {data2}\n CHICKEN TENDER: {data3}\n CHICKEN SALAD: {data4}\n PUMPKIN SOUP: {data5}\n SALAD: {data6}\n PIZZA: {data7}\n")
        mycursor.close()

    def table3():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM selected WHERE id = 10")
        result = mycursor.fetchone()
        
        data2 = result[1]
        data3 = result[2]
        data4 = result[3]
        data5 = result[4]
        data6 = result[5]
        data7 = result[6]
        messagebox.showinfo("ORDER-3",f"CHICKEN AND EGG: {data2}\n CHICKEN TENDER: {data3}\n CHICKEN SALAD: {data4}\n PUMPKIN SOUP: {data5}\n SALAD: {data6}\n PIZZA: {data7}\n")
        mycursor.close()

    def table4():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM selected WHERE id = 9")
        result = mycursor.fetchone()
        
        data2 = result[1]
        data3 = result[2]
        data4 = result[3]
        data5 = result[4]
        data6 = result[5]
        data7 = result[6]
        messagebox.showinfo("ORDER-4",f"CHICKEN AND EGG: {data2}\n CHICKEN TENDER: {data3}\n CHICKEN SALAD: {data4}\n PUMPKIN SOUP: {data5}\n SALAD: {data6}\n PIZZA: {data7}\n")
        mycursor.close()

    def table5():
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM selected WHERE id = 8")
        result = mycursor.fetchone()
        
        data2 = result[1]
        data3 = result[2]
        data4 = result[3]
        data5 = result[4]
        data6 = result[5]
        data7 = result[6]
        messagebox.showinfo("ORDER-5",f"CHICKEN AND EGG: {data2}\n CHICKEN TENDER: {data3}\n CHICKEN SALAD: {data4}\n PUMPKIN SOUP: {data5}\n SALAD: {data6}\n PIZZA: {data7}\n")
        mycursor.close()

    def all_data():
        # Create a new window
        pop_up = tk.Toplevel()
        pop_up.title("All Data")
        
        # Create a table to display the data
        table = ttk.Treeview(pop_up)
        table['columns'] = ('name', 'price', 'image', 'outofstock')
        table.column('#0', width=0, stretch=tk.NO)
        table.column('name', anchor=tk.CENTER, width=150)
        table.column('price', anchor=tk.CENTER, width=100)
        table.column('image', anchor=tk.CENTER, width=100)
        table.column('outofstock', anchor=tk.CENTER, width=100)
        table.heading('name', text='Name')
        table.heading('price', text='Price')
        table.heading('image', text='Image')
        table.heading('outofstock', text='Out_of_Stock')
        
        # Retrieve data from the database and insert it into the table
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM selected_data")
        results = mycursor.fetchall()
        for row in results:
            table.insert('', tk.END, text=row[0], values=(row[1], row[2], row[3], row[4]))
        
        # Pack the table into the window
        table.pack(padx=5, pady=5)


    def all_orders():
        # Create a new window
        pop_up = tk.Toplevel()
        pop_up.title("All Orders")
        
        # Create a table to display the data
        table = ttk.Treeview(pop_up)
        table['columns'] = ('ID', 'Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6')
        table.column('#0', width=0, stretch=tk.NO)
        table.column('ID', anchor=tk.CENTER, width=100)
        table.column('Item1', anchor=tk.CENTER, width=150)
        table.column('Item2', anchor=tk.CENTER, width=150)
        table.column('Item3', anchor=tk.CENTER, width=150)
        table.column('Item4', anchor=tk.CENTER, width=150)
        table.column('Item5', anchor=tk.CENTER, width=100)
        table.column('Item6', anchor=tk.CENTER, width=100)
        table.heading('ID', text='ID')
        table.heading('Item1', text='CHICKEN AND EGG')
        table.heading('Item2', text='CHICKEN TENDER')
        table.heading('Item3', text='CHICKEN SALAD')
        table.heading('Item4', text='PUMPKIN SOUP')
        table.heading('Item5', text='SALAD')
        table.heading('Item6', text='PIZZA')
        
        # Retrieve data from the database and insert it into the table
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM selected")
        results = mycursor.fetchall()
        for row in results:
            table.insert('', tk.END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        
        # Pack the table into the window
        table.pack(padx=5, pady=5)
    
    app2 = tk.Tk()
    width= app2.winfo_screenwidth()               
    height= app2.winfo_screenheight()
    app_width = width // 2
    app_height = height
    app_geometry = f"{app_width}x{app_height}+{app_width}+0"
    app2.geometry(app_geometry)
    app2.configure(bg="white")
    app2.title("Kitchen Management")

    # Create left panel with three buttons
    left_panel = tk.Frame(master=app2, width=200, bg="white")
    left_panel.pack(side="left", fill="both")
    # Create left panel with three buttons
    right_panel = tk.Frame(master=app2, width=200, bg="white")
    right_panel.pack(side="right", fill="both")
    # Create a button for table 1
    table_1_button = tk.Button(master=left_panel, text="TABLE-1", font=("Helvetica", 18),bg="white", fg="black", command=table1)
    table_1_button.pack(side="top", pady=20)

    table_2_button = tk.Button(master=left_panel, text="TABLE-2", font=("Helvetica", 18),bg="white", fg="black", command=table2)
    table_2_button.pack(side="top", pady=20)

    table_3_button = tk.Button(master=left_panel, text="TABLE-3", font=("Helvetica", 18),bg="white", fg="black", command=table3)
    table_3_button.pack(side="top", pady=20)

    table_4_button = tk.Button(master=left_panel, text="TABLE-4", font=("Helvetica", 18),bg="white", fg="black", command=table4)
    table_4_button.pack(side="top", pady=20)

    table_5_button = tk.Button(master=left_panel, text="Guest List", font=("Helvetica", 18),bg="white", fg="black", command=scripts.n2)
    table_5_button.pack(side="top", pady=20)

    all_data = tk.Button(master=left_panel, text="All Data", font=("Helvetica", 18),bg="white", fg="black", command=all_data)
    all_data.pack(side="top", pady=20)

    all_orders = tk.Button(master=left_panel, text="All Orders", font=("Helvetica", 18),bg="white", fg="black", command=all_orders)
    all_orders.pack(side="top", pady=20)



#create an option for editing menu

    #create a single funtion food which will be called from every button
    def food(sql_query, id):
        window = tk.Toplevel()
        window.title("Food {id}")
        window.geometry("400x400")

        tk.Label(window, text="Enter yes if out of stock else no:").pack()
        out_of_stock_entry = tk.Entry(window)
        out_of_stock_entry.pack()

        tk.Label(window, text="Enter the price:").pack()
        price_entry = tk.Entry(window)
        price_entry.pack()

        sql_query
        # Create a function to update the data(To be called from the food() function))
        def updatedata(sql_query):
            # Get the values from the text boxes
            value1 = out_of_stock_entry.get()
            value2 = price_entry.get()
            value2 = int(value2)
            mycursorf1 = mydb.cursor()
            mycursorf1.execute(sql_query, (value1, value2))
            mydb.commit()
            print(mycursorf1.rowcount, "record(s) affected")
            print("Outofstock: " + str(value1) + ", New Price: " + str(value2))
        confirm_button = tk.Button(window, text="Confirm", command=lambda:[updatedata(sql_query), window.destroy(), showMessage("Data Edited!", timeout=500)])
        confirm_button.pack()
        

    def f1():
        id == 1
        sql_query = "UPDATE selected_data SET outofstock = %s, price = %s WHERE id = 1"
        food(sql_query, id)
    def f2():
        id == 2
        sql_query = "UPDATE selected_data SET outofstock = %s, price = %s WHERE id = 2"
        food(sql_query, id)
    def f3():
        id == 3
        sql_query = "UPDATE selected_data SET outofstock = %s, price = %s WHERE id = 3"
        food(sql_query, id)
    def f4():
        id == 4
        sql_query = "UPDATE selected_data SET outofstock = %s, price = %s WHERE id = 4"
        food(sql_query, id)
    def f5():
        id == 5
        sql_query = "UPDATE selected_data SET outofstock = %s, price = %s WHERE id = 5"
        food(sql_query, id)
    def f6():
        id == 6
        sql_query = "UPDATE selected_data SET outofstock = %s, price = %s WHERE id = 6"
        food(sql_query, id)
    menu = tk.Menu(app2, tearoff=0)

    call_specific_robot = tk.Menubutton(master=right_panel, text="Call Specific Robot", font=("Helvetica", 18), bg="white", fg="black")
    call_specific_robot.pack(side="top", pady=100)

    call_specific_robot.menu = tk.Menu(call_specific_robot, tearoff=0)
    call_specific_robot.menu.add_cascade(label="ROBOT 1",command=lambda: scripts.n1(1),font=("Helvetica", 20))
    call_specific_robot.menu.add_cascade(label="ROBOT 2",command=lambda: scripts.n1(2),font=("Helvetica", 20))
    call_specific_robot.menu.add_cascade(label="ROBOT 3",command=lambda: scripts.n1(3),font=("Helvetica", 20))
    call_specific_robot.menu.add_cascade(label="ROBOT 4",command=lambda: scripts.n1(4),font=("Helvetica", 20))
    call_specific_robot.menu.add_cascade(label="ROBOT 5",command=lambda: scripts.n1(5),font=("Helvetica", 20))

            

    call_any_robot = tk.Button(master=right_panel, text="Call Any Robot", font=("Helvetica", 18),command = scripts.robot_popup,bg="white", fg="black")
    call_any_robot.pack(side="top", pady=100, padx=100)
    

    edit_button = tk.Menubutton(master=right_panel, text="EDIT MENU", font=("Helvetica", 18), bg="white", fg="black")
    edit_button.pack(side="right", pady=100, padx=100)

    edit_button.menu = tk.Menu(edit_button, tearoff=0)
    edit_button.menu.add_cascade(label="Food 1", command=f1,font=("Helvetica", 20))
    edit_button.menu.add_cascade(label="Food 2", command=f2,font=("Helvetica", 20))
    edit_button.menu.add_cascade(label="Food 3", command=f3,font=("Helvetica", 20))
    edit_button.menu.add_cascade(label="Food 4", command=f4,font=("Helvetica", 20))
    edit_button.menu.add_cascade(label="Food 5", command=f5,font=("Helvetica", 20))
    edit_button.menu.add_cascade(label="Food 6", command=f6,font=("Helvetica", 20))

    call_specific_robot["menu"] = call_specific_robot.menu
    edit_button["menu"] = edit_button.menu

    app2.mainloop()



    
class SelectedData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), default='Sample')
    price = db.Column(db.Integer, default=0)
    image = db.Column(db.String(50), default='5.PNG')
    outofstock = db.Column(db.String(10), default='no')

class Selected(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id1 = db.Column(db.Integer, default=0)
    id2 = db.Column(db.Integer, default=0)
    id3 = db.Column(db.Integer, default=0)
    id4 = db.Column(db.Integer, default=0)
    id5 = db.Column(db.Integer, default=0)
    id6 = db.Column(db.Integer, default=0)



@app.route('/')
def index():
    products = SelectedData.query.all()
    return render_template('index.html',products=products)
threading.Thread(target=gui).start()
threading.Thread(target=tab).start()
@app.route('/save', methods=['POST'])
def save():
    arr = Selected(**request.json)
    db.session.add(arr)
    db.session.commit()
    return 'Confirmed successfully!'

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1.25, open_browser).start()
    app.run(host='0.0.0.0',port = 5000)    