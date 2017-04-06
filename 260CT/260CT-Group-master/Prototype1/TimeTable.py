'''
Sphere Booking and Check-in
260CT
prototype
Salah Abdo
Python 3
'''
from home import *

class timeTable():

    def __init__(self,master,mainwnd):

        self.mainwnd= mainwnd # store the 'self.master` of the main window
        self.master = master

        self.master.geometry("600x500+200+200") # size of the window
        self.master.title("Sphere Booking and Check-in")
        
        self.master.date = StringVar()
        self.master.ID = StringVar()

        self.label1=Label(self.master,text="Sphere Booking and Check-in",fg="black",font=("Helvetica",25))
        
        self.label2=Label(self.master,text="date:",fg="black", font=("Helvetica",12, "bold italic"))
        self.label3=Label(self.master,text="Staff ID:",fg="black", font=("Helvetica",12, "bold italic"))

        self.input1=Entry(self.master, textvariable=self.master.date)
        self.input2=Entry(self.master, textvariable=self.master.ID)

        self.button1=Button(self.master,text="Slope",fg="black",width=10, height=1,command=self.slopeOp)
        self.button2=Button(self.master,text="instructor",fg="black",width=10, height=1,command=self.instruct)
        self.button3=Button(self.master,text="Home",fg="black",width=10, height=1,command=self.home)

        self.label1.pack(side="top",padx=15,pady=15)
        
        self.label2.pack(side="top",padx=15,pady=15)
        self.input1.pack(side="top",padx=15,pady=15)

        self.label3.pack(side="top",padx=15,pady=15)
        self.input2.pack(side="top",padx=15,pady=15)
        
        self.button1.pack(side="top", padx=15,pady=15)
        self.button2.pack(side="top", padx=15,pady=15)
        self.button3.pack(side="top", padx=15,pady=15)
        
        
    def home(self):
        self.master.destroy() # close the current Member window
        self.mainwnd.update() # update the home window
        self.mainwnd.deiconify()

    def slopeOp(self):

        self.master.withdraw()
        date = self.input1.get()
        runSlope= Maketimetable(date)
        printTimeTable(runSlope)

    def instruct(self):

        self.master.withdraw()
        date = self.input1.get()
        iid = self.input2.get()
        runInstruct = MaketimetableI(date,iid)
        printTimeTable(runInstruct)
