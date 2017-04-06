'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3
'''
from Main import *

class updateMember():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master= master
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="First Name").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Surname").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Date of birth").grid(row=6)
        Label(self.master, text="    ").grid(row=7)


        self.e1 = Entry(self.master)
        self.e2 = Entry(self.master)
        self.e3 = Entry(self.master)

        self.e1.grid(row=2, column=1)
        self.e2.grid(row=4, column=1)
        self.e3.grid(row=6, column=1)


        Button(self.master, text='Update', command=self.checkValue, font=("Helvetica",15, "bold italic")).grid(row=11, column=2, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=2, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window

    def closeDB(self):
        self.c.close()
        self.conn.close()

    def updateMember(self):
        customerID = self.customer
        sessionNum = self.sessionNum
        loyalty = "loyalty"

        if sessionNum > 10: # check to see if the user meets the requirements to upgrade their membership
            self.c.execute("UPDATE Member SET Membership_Type = (?) WHERE Customer_ID = (?) ", # find the customer in the database and updates his membership status
                       (loyalty, customerID))
            self.conn.commit()
            self.closeDB()
        else:
            print("user does not have more than 10 sessions")
            print(sessionNum)
            
        
    def checkValue(self):

        firstName = self.e1.get()
        surname = self.e2.get()
        dob = self.e3.get()
        
        self.c.execute("SELECT CustomerID FROM Customer WHERE FirstName = ? AND surname = ? AND date_of_birth = ?",
                       (firstName, surname, dob))
        self.ID = self.c.fetchone()
        self.customer = str(self.ID[0])

        self.c.execute("SELECT number_of_sessions FROM Customer WHERE FirstName = ? AND surname = ? AND date_of_birth = ?",
                       (firstName, surname, dob))

        session = self.c.fetchone()
        self.sessionNum = int(session[0])
        
        self.updateMember()   
        

class regMember():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master.geometry("1080x800+200+200")
        self.master.title("Sphere Booking and Check-in")

        self.conn = sqlite3.connect('Database.db')
        self.c = self.conn.cursor()

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        Label(self.master, text="    ").grid(row=1)
        Label(self.master, text="First Name").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Surname").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Date of birth").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        Label(self.master, text="Date").grid(row=2,column=2)
        Label(self.master, text="    ").grid(row=3)

        self.MFname = Entry(self.master)
        self.MSname = Entry(self.master)
        self.Mdob = Entry(self.master)
        self.Mdate = Entry(self.master)

        self.MFname.grid(row=2, column=1)
        self.MSname.grid(row=4, column=1)
        self.Mdob.grid(row=6, column=1)
        self.Mdate.grid(row=2, column=3)

        Button(self.master, text='Create membership', command=self.checkValue, font=("Helvetica",15, "bold italic")).grid(row=11, column=4, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=12, column=4, sticky=W, pady=4)

    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window

    def closeDB(self):
        self.c.close()
        self.conn.close()
        self.goHome()
        
    def insertMember(self):
        customerID = int(self.customerID)
        date = self.Mdate.get()
        membershipType = "standard"
        membership = self.memID  
        
        self.c.execute("INSERT INTO Member ( Membership_ID, Customer_ID, Membership_Type, Join_Date) VALUES (?, ?, ?, ?)",
                       (membership, customerID, membershipType, date,))
        self.conn.commit()

        self.closeDB()
        
    def randomMemberID(self):
        range_start = 10**(10-1)
        range_end = (10**10)-1
        self.memID = randint(range_start, range_end)
        
        self.insertMember()
        
    def checkValue(self):

        firstName = self.MFname.get()
        surname = self.MSname.get()
        dob = self.Mdob.get()
        
        self.c.execute("SELECT CustomerID FROM Customer WHERE FirstName = ? AND surname = ? AND date_of_birth = ?",
                       (firstName, surname, dob))
        self.ID = self.c.fetchone()
        
        self.customerID = self.ID[0]
        
        self.randomMemberID()  
    
