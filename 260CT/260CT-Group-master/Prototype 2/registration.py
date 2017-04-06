import tkinter
import sqlite3
from tkinter import *
from tkinter import ttk


class App():

    def __init__ (self, master):

        frame = Frame(master)
        frame.pack()

        
        # Set variable and variable type
        
        self.foreName = StringVar()
        self.surName = StringVar()
        self.doBirth = StringVar(frame, value="DD/MM/YYYY")    #Set default value format for date
        self.customerExp = StringVar()
        self.accountStat = StringVar()
        self.numberSess = StringVar()
        self.balance = StringVar(frame, value="0")             #Set default balance to 0

        
        self.foreName1 = StringVar()
        self.surName1 = StringVar()
        self.doBirth1 = StringVar()
        self.customerExp1 = StringVar()
        self.accountStat1 = StringVar()
        self.numberSess1 = StringVar()
        self.balance1 = StringVar()

        # Open database connection
        
        self.conn = sqlite3.connect('Database.db')            
        self.cur = self.conn.cursor()
        print('Database Opened Successfully')

        # GUI Button
        
        self.button2 = Button (frame, text = 'Insert Data', command = self.insertDb)
        self.button2.grid(row = 10, column = 1)

        self.button3 = Button(frame, text='Quit', command=self.quitDB)
        self.button3.grid(row=10, column=2)

        #GUI Entry and Label for user input

        self.l2 = Label(frame, text = "First Name")
        self.l2.grid(row = 3, column = 0)
        self.foreName = Entry(frame, bd = 6)
        self.foreName.grid(row = 3, column = 1)

        self.l3 = Label(frame, text = "Surname")
        self.l3.grid(row = 4, column = 0)
        self.surName = Entry(frame, bd = 7)
        self.surName.grid(row = 4, column = 1)

        self.l4 = Label(frame, text = "Date of Birth")
        self.l4.grid(row = 5, column = 0)
        self.doBirth = Entry(frame, textvariable=self.doBirth,bd = 8)
        self.doBirth.grid(row = 5, column = 1)

        self.l5 = Label(frame, text = "Customer Experience")
        self.l5.grid(row = 6, column = 0)
        self.cb1 = Checkbutton(frame, text="Novice", variable = self.customerExp, onvalue = "Novice", offvalue = "None",bd = 9)     # Checkbutton user input
        self.cb2 = Checkbutton(frame, text="Member", variable = self.customerExp, onvalue = "Member", offvalue = "None",bd = 10)
        self.cb1.grid(row = 6, column = 1)
        self.cb2.grid(row = 7, column = 1)
        

        self.l7 = Label(frame, text = "Number of Session")
        self.l7.grid(row = 8, column = 0)
        self.numberSess = Entry(frame, bd = 11)
        self.numberSess.grid(row = 8, column = 1)

        self.l8 = Label(frame, text = "Account Balance")
        self.l8.grid(row = 9, column = 0)
        self.balance = Entry(frame, textvariable=self.balance,bd = 12)
        self.balance.grid(row = 9, column = 1)


    def insertDb(self):                 # Function for inserting user input to the database
        
        
        foreName1 = self.foreName.get() 
        surName1 = self.surName.get()
        doBirth1 = self.doBirth.get()
        customerExp1 = self.customerExp.get()
        numberSess1 = int(self.numberSess.get())
        balance1 = int(self.balance.get())

        # SQL Function for inserting input to database
        
        self.cur.execute("INSERT INTO Customer \
(CustomerID, FirstName, surname, date_of_birth, customer_experience, number_of_sessions, balance_owed)\
VALUES (NULL, ?, ?, ?, ?, ?, ?)", (foreName1, surName1, doBirth1, customerExp1, numberSess1, balance1))

        self.conn.commit()
        print("Data has been successfully entered")


    def quitDB(self):                   # Function for user to quit program
        root.quit()
        self.conn.close()
        print("Database is now Closed")




        
def run():
    root = tkinter.Tk()
    root.title("Sphere Registration Table")
    root.geometry('700x400')

    app = App(root)
    root.mainloop()


