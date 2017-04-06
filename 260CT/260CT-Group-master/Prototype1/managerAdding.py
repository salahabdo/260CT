import sys
import sqlite3 as sql
from tkinter import *

def ManagerAdd():
        global IDb
        global forenameB
        global surnameB
        global positionB
        global sqliteFile
        sqliteFile = 'Database.db'
        roots =Tk()
        roots.title('Add manager')

        Title1 = Label(roots, text='Please enter manager details:')
        Title1.grid(row=0, column=0, sticky=E)

        forename = Label(roots,text='Enter Forename: ')
        surname = Label(roots,text='Enter Surename: ')
        position = Label(roots,text='Enter Position: ')
        ID = Label(roots, text='Enter ID: ')

        ID.grid(row=1, column=0, sticky=W)
        forename.grid(row=2, column=0, sticky=W)
        surname.grid(row=3, column=0, sticky=W)
        position.grid(row=4, column=0, sticky=W)

        surnameB = Entry(roots)    
        forenameB = Entry(roots)
        positionB = Entry(roots)
        IDb = Entry(roots)

        IDb.grid(row=1, column=1)
        forenameB.grid(row=2, column=1)
        surnameB.grid(row=3, column=1)
        positionB.grid(row=4, column=1)

        Add = Button(roots, text='Add to database', command=AddF)
        Add.grid(row=5, column=0, sticky=W)
        roots.mainloop()
def AddF():
        userInput1 = IDb.get()
        userInput2 = forenameB.get()
        userInput3 = surnameB.get()
        userInput4 = positionB.get()
        try:
                con = sql.connect(sqliteFile)
                cur = con.cursor()
                person = [(userInput1, userInput2, userInput3, userInput4)]
                cur.executemany('''INSERT INTO Managers (StaffID, Forename, Surname, Position) VALUES (?,?,?,?)''', person)
                con.commit()

        finally:
                con.close()

