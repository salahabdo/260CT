'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3

This code is for the booking. 
'''

from Main import *
from TimeTable import *
from home import *

class Booking(object):

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        self.ref = "  "
        self.price = 0
        self.date = "  "
        self.time = "  "
        
        self.master.geometry("1080x800")
        self.master.title("Sphere Booking and Check-in")

        self.conn = sqlite3.connect('Database.db') # connects to the database
        self.c = self.conn.cursor()

        self.time = StringVar(self.master)
        self.time.set("Select") # initial value

        self.day = StringVar(self.master)
        self.day.set("Select") # initial value
        
        self.day2 = StringVar(self.master)
        self.day2.set("Select") # initial value

        self.month = StringVar(self.master)
        self.month.set("Select") # initial value
        
        self.month2 = StringVar(self.master)
        self.month2.set("Select") # initial value

        self.year = StringVar(self.master)
        self.year.set("Select") # initial value
        
        self.year2 = StringVar(self.master)
        self.year2.set("Select") # initial value

        self.session = StringVar(self.master)
        self.session.set("Select") # initial value
        

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        
        Label(self.master, text="Custromer Information",fg="black",font=("Helvetica",11,'bold')).grid(row=1)
        Label(self.master, text="First Name:").grid(row=2)
        Label(self.master, text="    ").grid(row=3)
        Label(self.master, text="Surname:").grid(row=4)
        Label(self.master, text="    ").grid(row=5)
        Label(self.master, text="Date of birth: ").grid(row=6)
        Label(self.master, text="    ").grid(row=7)
        
        Label(self.master, text="Booking Information",fg="black",font=("Helvetica",11,'bold')).grid(row=1, column=3)
        Label(self.master, text="Session:").grid(row=2, column=3)
        Label(self.master, text="    ").grid(row=3, column=3)
        Label(self.master, text="Time: ").grid(row=4, column=3)
        Label(self.master, text="    ").grid(row=5, column=3)
        Label(self.master, text="Date:").grid(row=6, column=3)
        Label(self.master, text="    ").grid(row=7, column=3)
        
        self.firstName = Entry(self.master)
        self.surname = Entry(self.master)
        # stores the entry made into a variable 
        
        session = OptionMenu(self.master, self.session, "normal", "instructor") 
        time = OptionMenu(self.master, self.time, "8:00", "10:00", "12:00", "14:00", "16:00", "18:00")
        year = OptionMenu(self.master, self.year, "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025","2026","2027","2028","2029","2030","2031","2032","2033","2034","2035")
        month = OptionMenu(self.master, self.month, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        day = OptionMenu(self.master, self.day, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")

        year2 = OptionMenu(self.master, self.year2, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017)
        month2 = OptionMenu(self.master, self.month2, "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        day2 = OptionMenu(self.master, self.day2, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        #drop down select menue
        

        self.firstName.grid(row=2, column=1)
        self.surname.grid(row=4, column=1)
        day2.grid(row=6, column=1)
        month2.grid(row=7, column=1)
        year2.grid(row=8, column=1)
        
        session.grid(row=2, column=4)
        day.grid(row=6, column=4)
        time.grid(row=4, column=4)
        month.grid(row=7, column=4)
        year.grid(row=8, column =4)
        
        # positioning of the entry 

        Button(self.master, text='Book', command=self.confirmation, font=("Helvetica",15, "bold italic")).grid(row=11, column=4, sticky=W, pady=4)
        Button(self.master, text='Timetable', command=self.table, font=("Helvetica",15, "bold italic")).grid(row=12, column=4, sticky=W, pady=4)
        Button(self.master, text='Home', command=self.goHome, font=("Helvetica",15, "bold italic")).grid(row=13, column=4, sticky=W, pady=4)

        # padx = horizonta
        # pady = verticle
        # .grid(row=6, column=2)
        # row = increase the number you move down, decrease the number  you move up.
        # column = increase the number you move right, decrease the number you move left.

    def table(self):
        root=Toplevel(self.master)
        timetable=timeTable(root,self.master)
        # Opens the slope or instructor timetable


    def goHome(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify() # un-minimize the home window
        
    def bookingConfirmation(self):
        root1=Toplevel(self.master)
        bookingcon=BookingConfirmation(root1,self.master,self.ref,self.date,self.time,self.price)
        
    def closeDB(self): # closes the database
        self.c.close()
        self.conn.close()
        self.bookingConfirmation()

    def insertBooking(self):
        refNum = self.ref
        customerID = self.customer
        day = self.day.get()
        year = self.year.get()
        month = self.month.get()
        self.time = self.time.get()
        checking = "False"
        price = self.price
        sessionNumber = self.sessionNum
        session = self.session.get()

        dash = "-"
        self.date = year + dash + month + dash + day #concatenates day month and year into required format "2017-03-23"

        self.c.execute("INSERT INTO Booking (Ref_number, customerID, session, date, time, checking, price) VALUES(?, ?, ?, ?, ?, ?, ?)", # stores all the data into booking table 
                       (refNum, customerID, session, self.date, self.time, checking, price))                     
        
        self.c.execute("UPDATE Customer SET number_of_sessions = (?) WHERE CustomerID = (?) ",
                       (sessionNumber, customerID))
        self.conn.commit()
        
        self.closeDB()

    def id_generator(self,size=16, chars=string.ascii_uppercase + string.digits): # Creates a random 16 digit value with numbers and characters, used as reference number
        self.ref=''.join(random.choice(chars) for _ in range(size))
        self.insertBooking()

    def calculate(self):
        session = self.session.get()
        cID = self.customer
        
        normal = 50 # price per hour
        instructor = 20 #price per hour
        self.price = 0

        self.c.execute("SELECT count(1) FROM Member WHERE Customer_ID = ?", # selects what membership the customer had, this will be used to calculate the price
                   (cID))
        membershipCheck = self.c.fetchone()
        numberCheck = int(membershipCheck[0])

        if numberCheck == 1:
            self.c.execute("SELECT Membership_Type FROM Member WHERE Customer_ID = ?", # selects what membership the customer had, this will be used to calculate the price
                   (cID))
        
            membershipType = True
        
        else:
            membershipType = False

        # If customer has normal membership or no membership then no discount
        if membershipType == False: # use the customers membership to give a discount if they have loyalty membership
            if session.lower() == "normal":
                self.price = normal
            else:
                self.price = normal + instructor
                
        # if customer has the correct membership then they get a discount
        else:
            if session.lower() == "normal":
                discount = (normal * 20) / 100 #gives 20% off the price since the customer has a loyalty membership
                self.price = normal - discount
                
            else:
                discount = (normal + instructor * 20) / 100
                self.price = normal + instructor - discount

        self.id_generator()
        
            
    def getUserInfo(self):

        self.c.execute("SELECT CustomerID FROM Customer WHERE FirstName = ? AND surname = ? AND date_of_birth = ?", # Get customer ID from the data base where the customer name, surname and date of birth matches.
                       (self.firstName, self.surname, self.dob))
        self.ID = self.c.fetchone()
        self.customer = str(self.ID[0])

        self.c.execute("SELECT number_of_sessions FROM Customer WHERE FirstName = (?) AND surname = (?) AND date_of_birth = (?)", # Get the amount of sessions the customer has booked from the customer table
                       (self.firstName, self.surname, self.dob))

        session = self.c.fetchone() 
        self.sessionNum = int(session[0])
        self.sessionNum +=1
        
        self.calculate()
    
    def noCustomer(self): 
        root2=Toplevel(self.master)
        self.master.withdraw()
        customer=CustomerNotFound(root2,self.master)

    def wrongEntry(self):
        root3=Toplevel(self.master)
        self.master.withdraw()
        entry=bookingError(root3,self.master)
        

    def checkEntry(self):
        day = self.day.get()
        y = self.year.get()
        month = self.month.get()
        time = self.time.get()
        session = self.session.get()

        if session != "Select":
            if time != "Select":
                if day != "Select":
                    if month != "Select":
                        if y != "Select":
                            self.getUserInfo()
        else:
            self.wrongEntry()
            
        

    def confirmation(self):

        self.firstName = self.firstName.get()
        self.surname = self.surname.get()
        
        day = self.day2.get()
        y = self.year2.get()
        month = self.month2.get()
        dash = "-"
        year = str(y)

        self.dob = year + dash + month + dash + day #concatenates day month and year into required format "2017-03-23"
        
        self.c.execute("SELECT count(1)FROM Customer WHERE FirstName = (?) AND surname = (?) AND date_of_birth = (?)", # Get the amount of sessions the customer has booked from the customer table
                       (self.firstName, self.surname, self.dob))

        confirmation = self.c.fetchone()
        checkConf = int(confirmation[0])

        if checkConf == 1:
            self.checkEntry()
        else:
            self.noCustomer()
            
    

class BookingConfirmation(object):

    def __init__(self,master,mainwnd,ref,date,time,price):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.bookingRef = ref # variables passed between classes
        self.date = date
        self.time = time
        self.price = price
        

        self.master.geometry("500x400") # size of the window
        self.master.resizable (0, 0) #disables resizing

        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)

        Label(self.master, text="The booking has been successful.\nBooking reference: " + str(self.bookingRef) + "\nDate: " + str(self.date) + "\nTime: " + str(self.time) + "\nPrice: £" + str(self.price),fg="red",font=("Helvetica",14)).grid(row=2,column=2)
        Label(self.master, text="   ").grid(row=3,column=2)
        


class CustomerNotFound():

    def __init__(self,master,mainwnd):
        
        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master.geometry("500x400") # size of the window
        self.master.resizable (0, 0) #disables resizing
        self.master.title("Sphere Booking and Check-in")
        
        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        
        Label(self.master, text="The customer does not exist, either register the customer\nor try the booking again.",fg="red",font=("Helvetica",14)).grid(row=2,column=2)
        
        self.button1=Button(self.master,text="Register new customer", command=self.register, fg="black", width=20, height=3,font=("Helvetica",15, "bold italic")).grid(row=4, column=2)
        self.button1=Button(self.master,text="Booking", command=self.gotoBooking, fg="black", width=20, height=3,font=("Helvetica",15, "bold italic")).grid(row=5, column=2)

        
    def gotoBooking(self):

        root1=Toplevel(self.master)
        self.master.withdraw()
        booking=Booking(root1,self.master)
            
    def register(self):
        
        self.master.withdraw()
        run()

class bookingError():

    def __init__(self,master,mainwnd):
        
        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master
        
        self.master.geometry("500x400") # size of the window
        self.master.resizable (0, 0) #disables resizing
        self.master.title("Sphere Booking and Check-in")
        
        Label(self.master, text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25)).grid(row=0,column=2)
        
        Label(self.master, text="Please double check to make sure you have\n entered everything correctly.",fg="red",font=("Helvetica",14)).grid(row=2,column=2)
        
        self.button1=Button(self.master,text="Booking", command=self.gotoBooking, fg="black", width=20, height=3,font=("Helvetica",15, "bold italic")).grid(row=5, column=2)

        
    def gotoBooking(self):

        root1=Toplevel(self.master)
        self.master.withdraw()
        booking=Booking(root1,self.master)


    

            

        
        
    
