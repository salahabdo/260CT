from tkinter import *
import os
import sqlite3
import sys



def deleteId():
    global idE
    global roots

    roots=Tk()
    roots.title('Remove An Account Menu')
    subTitle= Label(roots, text='Please enter the customer details below')
    subTitle.grid(row=0, column=0, sticky=E)
    
######################### THE LABELS ###########################################
    idL= Label(roots,text='Enter Customer ID: ')
    idL.grid(row=1, column=0, sticky=W)

    
######################### THE BOXES #############################################
    idE= Entry(roots)    
    idE.grid(row=1, column=1)

#########################  THE BUTTONS #############################################
    closeButton = Button(roots, text='Close', command=closeWindow) # CLOSE WINDOW
    closeButton.grid(row=5, column=0, sticky=W)
    removeButton = Button(roots, text='Remove User?', command=checkIfdelete) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    removeButton.grid(row=5, column=1, sticky=W)
    roots.mainloop()

def closeWindow():
    roots.destroy()

    
def checkIfdelete():
    

    userId= idE.get()

    
############### SQL DATABASE RETRIEVE AND DELETE ##################################
    connection = sqlite3.connect("Database.db")
    remove= connection.execute("DELETE FROM User_Names WHERE ID =? ", (userId))
    sql1= connection.execute("DELETE FROM Customer_Details WHERE ID = ? ",(userId))
    result=connection.execute("SELECT * FROM Customer_Details, User_Names")
    connection.commit()
    print("row deleted: ", connection.total_changes)
    
        
    if userId!=(len(result.fetchall())>0):#see if input is correct
        r=Tk()
        r.geometry('160x65')
        rlbl=Label(r,text='the user has been deleted')
        rlbl.pack()
        r.mainloop()
        

    connection.close()   
    roots.destroy()    
deleteId()

