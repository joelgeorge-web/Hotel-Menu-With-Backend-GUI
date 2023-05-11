import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="db"
    )

def robot_popup():
        print("  _____ ")
        print(" /     \\")
        print("| () () |")
        print("|  |||  |")
        print(" \\'_'_/ ")
        print("  / | \\ ")
        print(" |  |  |")
        print(" |  |  |")

def n1(id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM robot WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    for row in results:
        print("Id: " + str(row[0]) + ", Robot Name: " + str(row[1]), "Unique Code: " + str(row[2]))





def n2():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM guest"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for row in results:
        print(" Name: " + str(row[1]), "Phone no: " + str(row[2]), "no of guest: " + str(row[3]))