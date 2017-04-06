import sys
import sqlite3 as sql
from random import randint
from tkinter import *

class ManagerAdd():
        def __init__(self):
                #Declare global variables
                global IDb
                global forenameB
                global surnameB
                global sqliteFile
                global PosSelect
                sqliteFile = 'Database.db'
                #Create the window
                roots =Tk()
                roots.title('Add staff')
                #Create the Labels
                Title1 = Label(roots, text='Please enter new staff details:')
                Title1.grid(row=0, column=0, sticky=E)
                forename = Label(roots,text='Enter Forename: ')
                surname = Label(roots,text='Enter Surename: ')
                position = Label(roots,text='Enter Position: ')
                #Position the Labels
                forename.grid(row=1, column=0, sticky=W)
                surname.grid(row=2, column=0, sticky=W)
                position.grid(row=3, column=0, sticky=W)
                #Create the entry fields
                surnameB = Entry(roots)    
                forenameB = Entry(roots)
                PosSelect = StringVar(roots)
                PosSelect.set("Manager")
                positionB = OptionMenu(roots, PosSelect, "Manager","Instructor","Slope Operator")
                #Position the Entry Fields
                forenameB.grid(row=1, column=1)
                surnameB.grid(row=2, column=1)
                positionB.grid(row=3, column=1)
                #Create the submit button
                Add = Button(roots, text='Submit', command=self.AddF)
                Add.grid(row=5, column=0, sticky=W)
                roots.mainloop()
        def AddF(self):
                Input = randint(0,9999)       #Generate a random number for the ID
                userInput2 = forenameB.get()
                userInput3 = surnameB.get()
                userInput4 = PosSelect.get()
                try:
                        #Connect to database
                        con = sql.connect(sqliteFile)
                        cur = con.cursor()
                        #Commit to database
                        person = [(Input, userInput2, userInput3, userInput4)]
                        cur.executemany('''INSERT INTO Managers (StaffID, Forename, Surname, Position) VALUES (?,?,?,?)''', person)
                        con.commit()

                finally:
                        #Close database
                        con.close()

