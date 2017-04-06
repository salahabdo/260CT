from tkinter import *
import tkinter
import sqlite3


class App():

    def __init__ (self, master):

        frame = Frame(master)
        frame.pack()

        staffID = StringVar()
        foreName = StringVar()
        surName = StringVar()
        position = StringVar()


        staffID1 = StringVar()
        foreName1 = StringVar()
        surName1 = StringVar()
        position1 = StringVar()


        self.button = Button (frame, text = 'Open Database', fg = 'red', command = self.openDb)
        self.button.grid(row = 0, column = 0)

        self.button2 = Button (frame, text = 'Update Data', command = self.updateDb)
        self.button2.grid(row = 0, column = 1)

        self.button3 = Button (frame, text = 'Close Database', command = self.closeDB)
        self.button3.grid(row = 0, column = 2)

        self.l1 = Label(frame, text = "ID")
        self.l1.grid(row = 2, column = 0)
        self.staffID = Entry(frame, bd = 6)
        self.staffID.grid(row = 2, column = 1)
        
        self.l2 = Label(frame, text = "Forename")
        self.l2.grid(row = 3, column = 0)
        self.foreName = Entry(frame, bd = 6)
        self.foreName.grid(row = 3, column = 1)

        self.l3 = Label(frame, text = "Surname")
        self.l3.grid(row = 4, column = 0)
        self.surName = Entry(frame, bd = 7)
        self.surName.grid(row = 4, column = 1)

        self.l4 = Label(frame, text = "Position")
        self.l4.grid(row = 5, column = 0)
        self.position = Entry(frame, bd = 8)
        self.position.grid(row = 5, column = 1)

    def openDb(self):
        
        self.conn = sqlite3.connect('Database.db')
        self.cur = self.conn.cursor()
        print('Database Opened Successfully')


    def updateDb(self):

        staffID1 = int(self.staffID.get())
        foreName1 = self.foreName.get() 
        surName1 = self.surName.get()
        position1 = self.position.get()
        
        self.cur.execute("UPDATE Managers SET Forename = ?, Surname = ?, Position = ? WHERE StaffID = ?"\
                         , (foreName1, surName1, position1, staffID1))
        print("Data Updated")

        self.conn.commit()


    def closeDB(self):
        
        self.conn.close()
        print("Database is now Closed")
        

def runUpdate ():
    root = tkinter.Tk()
    root.title("Sphere Registration Table")
    root.geometry('700x400')

    app = App(root)
    root.mainloop()

