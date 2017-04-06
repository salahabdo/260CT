from tkinter import *
import os
import sqlite3
import sys



def deleteId():
    global staffIdE
    global roots

    roots=Tk()
    roots.title('Remove An Account Menu')
    subTitle= Label(roots, text='Please enter the staff details below')
    subTitle.grid(row=0, column=0, sticky=E)
    
######################### THE LABELS ###########################################
    staffIdL= Label(roots,text='Enter staff ID: ')
    staffIdL.grid(row=1, column=0, sticky=W)

    
######################### THE BOXES #############################################
    staffIdE= Entry(roots)    

    staffIdE.grid(row=1, column=1)

    
#########################  THE BUTTONS #############################################
    closeButton = Button(roots, text='Close', command=closeWindow) # CLOSE WINDOW
    closeButton.grid(row=5, column=0, sticky=W)
    removeButton = Button(roots, text='Remove staff?', command=checkIfdelete) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    removeButton.grid(row=5, column=1, sticky=W)
    roots.mainloop()

def closeWindow():
    roots.destroy()

    
def checkIfdelete():

    staffId= staffIdE.get()
#GET INPUTS THATS TYPED IN BOXES
    
############### SQL DATABASE RETRIEVE AND DELETE ##################################
    connection = sqlite3.connect("Database.db")
    remove= connection.execute("DELETE FROM Manager_Login WHERE STAFFID =? ", (staffId))#delete from the table 
    sql1= connection.execute("DELETE FROM Managers WHERE STAFFID =? ",(staffId))#deletes from the table 
    result=connection.execute("SELECT * FROM Managers, Manager_Login")#used to check if staff is still in the tables 
    connection.commit()
    print("row deleted: ", connection.total_changes)
        
    if staffId!=(len(result.fetchall())>0):#checks if the staff have been removed.
        
        #see if input is correct
        r=Tk()
        r.geometry('160x65')
        rlbl=Label(r,text='the staff has been deleted')
        rlbl.pack()
        r.mainloop()
        

    connection.close()   
    roots.destroy()
deleteId()

