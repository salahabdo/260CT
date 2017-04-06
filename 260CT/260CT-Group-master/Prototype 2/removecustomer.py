from tkinter import *
import os
import sqlite3
import sys



def deleteId():
    global idE
    global nameE
    global sureNameE
    global dobE
    global roots

    roots=Tk()
    roots.title('Remove An Account Menu')
    subTitle= Label(roots, text='Please enter the customer details below')
    subTitle.grid(row=0, column=0, sticky=E)
    
######################### THE LABELS ###########################################
    idL= Label(roots,text='Enter Customer ID: ')
    nameL= Label (roots,text='Enter Name: ')
    sureNameL= Label (roots,text='Enter Surename: ')
    dobL= Label (roots,text='Enter Date Of Birth: ')
    idL.grid(row=1, column=0, sticky=W)
    nameL.grid(row=2, column=0, sticky=W)
    sureNameL.grid(row=3, column=0, sticky=W)
    dobL.grid(row=4, column=0, sticky=W)

    
######################### THE BOXES #############################################
    idE= Entry(roots)
    nameE= Entry(roots)
    sureNameE=Entry(roots)
    dobE=Entry(roots)
    idE.grid(row=1, column=1)
    nameE.grid(row=2, column=1)
    sureNameE.grid(row=3, column=1)
    dobE.grid(row=4, column=1)

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
    nameId= nameE.get()
    surenameId= sureNameE.get()
    dobId= dobE.get()

    
############### SQL DATABASE RETRIEVE AND DELETE ##################################
    connection = sqlite3.connect("Database.db")
    sql1= connection.execute("DELETE FROM Customer WHERE CustomerID = ? AND FirstName = ? AND surname = ? AND date_of_birth = ?",(userId, nameId, surenameId, dobId))
    result=connection.execute("SELECT * FROM Customer")
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

