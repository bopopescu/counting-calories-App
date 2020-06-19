import os
from tkinter import *
import mysql.connector
import csv



#Conect mysql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "haslo123",
    database = "products",
)

#Create a cursor
my_cursor = mydb.cursor()

#Crate database
#my_cursor.execute("CREATE DATABASE products")

#Ckecking my data base is woring
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)


# Created table for products

# #Create table
# my_cursor.execute("CREATE TABLE produkty  (name VARCHAR(255),\
#
#     weight INT(10),\
#     protein INT(10),\
#     carbs INT(10),\
#     fats INT(10),\
#     cal_per_100 INT(10),\
#     product_id INT AUTO_INCREMENT PRIMARY KEY)")

# Create table for login and password

# #Create table
# my_cursor.execute("CREATE TABLE LoginData (login VARCHAR(255),\
#     password VARCHAR(255),\
#     product_id INT AUTO_INCREMENT PRIMARY KEY)")

# Create login Window
def login_Window():
    log = Tk()
    log.title("Login")
    log.geometry("300x300")
    log.configure(background='gray')

    password_lbl = Label(text="Password",font=10, pady=10, bg='gray')
    password_lbl.grid(row=1, column=1, columnspan=2, padx=115,)
    password_box = Entry(log, bg='sandy brown')
    password_box.grid(row=2, column=1, columnspan=2)

    login_lbl = Label(text="Login", font=10, bg='gray')
    login_lbl.grid(row=3, column=1, columnspan=2)
    login_box = Entry(log, bg='sandy brown')
    login_box.grid(row=4, column=1, columnspan=2)

    def log_in():
        global haslo
        global login

        lista = []
        # result = my_cursor.fetchall()
        searched =(login_box.get())

        sql = "SELECT * from LoginData WHERE login = %s "
        name =(searched,)
        result = my_cursor.execute(sql,name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."

        
        for i in result:
            login = i[0]
            haslo = i[1]

        if haslo == password_box.get() and login == login_box.get():
            x = True

        if x is True:
            log.destroy()
            main_window()



    login_btn = Button(log, text="Log in", font=10, padx=40, command=log_in, bg='sky blue')
    login_btn.grid(row=5, column=1, pady=20, padx=85)

    def create_acc():
        sql_command = "INSERT INTO LoginData(login , password) VALUES (%s, %s)"
        values = (login_box.get(), password_box.get())

        my_cursor.execute(sql_command,values)
        mydb.commit()

        login_box.delete(0, END)
        password_box.delete(0, END)



    create_account_btn = Button(log, text="Create a Account", font=10, command=create_acc, bg='sky blue')
    create_account_btn.grid(row=6, column=1, padx=85)

    log.mainloop()

def Add_to_database():
    add_root = Tk()
    add_root.geometry("300x400")
    add_root.title("Add products to database")

    label = Label(add_root, text="Add new product", font=16, padx=10)
    label.grid(row=0, column=0)

    lbl_name = Label(add_root, text="Name ", font=10, pady=10)
    lbl_name.grid(row=1, column=0)
    lbl_weight =Label(add_root, text="Weight", font=10, pady=10)
    lbl_weight.grid(row=2, column=0)
    lbl_protein = Label(add_root, text="Protein", font=10, pady=10)
    lbl_protein.grid(row=3, column=0)
    lbl_carbs = Label(add_root, text="Carbs", font=10, pady=10)
    lbl_carbs.grid(row=4, column=0)
    lbl_fats = Label(add_root, text="Fats", font=10, pady=10)
    lbl_fats.grid(row=5, column=0)
    lbl_cel_per_100 = Label(add_root, text="Calorie per 100g ", font=10, pady=10)
    lbl_cel_per_100.grid(row=6, column=0)

    entry_name = Entry(add_root)
    entry_name.grid(row=1, column=1)
    entry_weight = Entry(add_root)
    entry_weight.grid(row=2, column=1)
    entry_protein = Entry(add_root)
    entry_protein.grid(row=3, column=1)
    entry_carbs = Entry(add_root)
    entry_carbs.grid(row=4, column=1)
    entry_fats = Entry(add_root)
    entry_fats.grid(row=5, column=1)
    entry_cel_per_100 = Entry(add_root)
    entry_cel_per_100.grid(row=6, column=1)


    def clear_fields():

        entry_name.delete(0, END )
        entry_weight.delete(0, END)
        entry_protein.delete(0, END)
        entry_carbs.delete(0,END)
        entry_fats.delete(0, END)
        entry_cel_per_100.delete(0, END)

    def add_product():
        sql_command = "INSERT INTO produkty (name, weight, protein, carbs, fats, cal_per_100) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (entry_name.get(), entry_weight.get(), entry_protein.get(), entry_carbs.get(), entry_fats.get(), entry_cel_per_100.get())

        my_cursor.execute(sql_command, values)

        mydb.commit()
        clear_fields()


    add_button = Button(add_root, text="Add product", padx=20, pady=5, command=add_product)
    add_button.grid(row=7, column=0, pady=10)

    add_root.mainloop()

kalorie1 = 0
protein1 = 0
wegle1 = 0
fats1 = 0

def main_window():

    root = Tk()
    root.title("Fitatu")
    root.geometry("350x550")
    root.configure(background='gray')
    first_lbl = Label(root, text=" Fit app !",font=("Helvetica",16),bg='grey')
    first_lbl.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

    ok_button = Button(root, text="Add to new product to database", font=10, width=35, command=Add_to_database,bg='sky blue')
    ok_button.grid(row = 1, column=0, pady=50, padx=10, columnspan=2)

    Add_here_lbl = Label(root, text="Add product ", font=10,bg='grey')
    Add_here_lbl.grid(row=2, column=0, sticky=N)

    lbl_name_root = Label(root, text="Name ", font=10, pady=10,bg='grey')
    lbl_name_root.grid(row=3, column=0)


    entry_getname_root = Entry(root, bg='sandy brown')
    entry_getname_root.grid(row=3, column=1, sticky=W)

    def find_product():
        searched = entry_getname_root.get()
        sql = "SELECT * FROM produkty WHERE name = %s"
        name = (searched,)
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()

        if not result:
            result = "Record Not Found..."

        searched_label = Label(root, text=result)
        searched_label.grid(row=4, column=1, padx=10)


    find_btn = Button(root, text="Find", font=10, padx=43, pady=2, command=find_product,bg='sky blue')
    find_btn.grid(row=4, column=0, pady=10)

    sumakal = 0


    # kalorie1 = 0
    # protein1 = 0
    # wegle1 = 0
    # fats1 = 0


    def add_product():

        global kalorie1
        global protein1
        global wegle1
        global fats1

        # kalorie1 = 0
        # protein1 = 0
        # wegle1 = 0
        # fats1 = 0

        global cal_100
        global bialko
        global wegle
        global tluszcz

        searched = entry_getname_root.get()

        sql = "SELECT protein FROM produkty WHERE name = %s"
        name = (searched,)
        protein = my_cursor.execute(sql, name)
        protein = my_cursor.fetchall()
        for i in protein:
            bialko = i[0]

        sql = "SELECT carbs FROM produkty WHERE name = %s"
        name = (searched,)
        carbs = my_cursor.execute(sql, name)
        carbs = my_cursor.fetchall()

        for i in carbs:
            wegle = i[0]

        sql = "SELECT fats FROM produkty WHERE name = %s"
        name = (searched,)
        fats = my_cursor.execute(sql, name)
        fats = my_cursor.fetchall()

        for i in fats:
            tluszcz = i[0]

        sql = "SELECT cal_per_100 FROM produkty WHERE name = %s"
        name = (searched,)
        cal_per_100 = my_cursor.execute(sql, name)
        cal_per_100 = my_cursor.fetchall()

        for i in cal_per_100:
            cal_100 = i[0]

        kalorie1 += int(entry_waga.get()) * 0.01 * cal_100
        protein1 += int(entry_waga.get()) * 0.01 * bialko
        wegle1 += int(entry_waga.get()) * 0.01 * wegle
        fats1 += int(entry_waga.get()) * 0.01 * tluszcz

        tabkal.config(text=kalorie1)
        tabprotein.config(text=protein1)
        tabcarbs.config(text=wegle1)
        tabfats.config(text=fats1)




    add_btn = Button(root, text="Add",font=10, padx=44, pady=3, command=add_product,bg='sky blue')
    add_btn.grid(row=5, column=0)

    entry_waga = Entry(root, bg='sandy brown')
    entry_waga.grid(row=5, column=1, pady=10, sticky=W)

    tab_kal = Label(root, text="Calories", font=10,bg='grey')
    tab_kal.grid(row=6, column=0, pady=10)
    tab_protein = Label(root, text="Protein",font=10,bg='grey')
    tab_protein.grid(row=7, column=0, pady=10)
    tab_carbs = Label(root, text="Carbs", font=10,bg='grey')
    tab_carbs.grid(row=8, column=0, pady=10)
    tab_fats = Label(root, text="Fats", font=10,bg='grey')
    tab_fats.grid(row=9, column=0, pady=10)


    tabkal = Label(root, text=0, font=10,bg='grey')
    tabkal.grid(row=6, column=1, pady=10, sticky=W)
    tabprotein = Label(root, text=0,font=10,bg='grey')
    tabprotein.grid(row=7, column=1, pady=10, sticky=W)
    tabcarbs = Label(root, text=0, font=10,bg='grey')
    tabcarbs.grid(row=8, column=1, pady=10, sticky=W)
    tabfats = Label(root, text=0, font=10,bg='grey')
    tabfats.grid(row=9, column=1, pady=10, sticky=W)

    root.mainloop()


login_Window()


