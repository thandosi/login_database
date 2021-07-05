
import mysql.connector
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Login")
root.geometry("400x400")

# start of label name
user_name = Label(root, text="Username: ")
user_name.place(x=10, y=20)
user_entry = Entry(root,)
user_entry.place(x=90, y=20, )


# start of label password
user_pass = Label(root, text="Password: ")
user_pass.place(x=10, y=60)
pass_entry = Entry(root, show="*")
pass_entry.place(x=90, y=60)
# end of password label


# login function
def login():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='hospital',
                                   auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    xy = mycursor.execute('Select * from login')
    for i in mycursor:
        if i[1] == pass_entry.get() and i[0] == user_entry.get():
            messagebox.showinfo("Output", "Login")
            root.destroy()
    if i[1] != pass_entry.get() or i[0] != user_entry.get():
            messagebox.showinfo("Output", "Enter correct information")
            pass_entry.delete(0, END)
            user_entry.delete(0, END)


# login button
login_btn = Button(root, text="Login", borderwidth="10", command=login, bg="royal blue")
login_btn.place(x=20, y=150)


# exit function
def register():
    mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                   database='hospital', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    sql = "INSERT INTO login (user, password) Value(%s, %s)"
    val = (user_entry.get(), pass_entry.get())
    mycursor.execute(sql, val)
    messagebox.showinfo("Output", "Registration Done.You can login.")
    pass_entry.delete(0, END)
    user_entry.delete(0, END)
    mydb.commit()


# exit button
exit_button = Button(root, text="Register", borderwidth="10", command=register, bg="royal blue")
exit_button.place(x=110, y=150)


root.mainloop()
