import sqlite3
import sys

def MaketimetableI(date, instructor):
    """will output a text based version of the timetable from database, assuming the database is in this file"""
    if len(date)>10: #statement to make injection attacks harder by stopping them writting anything longer then the required input 
        raise ValueError("This is longer then a date. What are you up to?")
    if len(instructor)>2: 
        raise ValueError("If we now have more then 99 staff members, please update the exception code in Ski Instructor Timetable, otherwise... What are you up to?")
    
    eightam= str(None) #preset the timetable variables as strings that are null(empty) 
    tenam= str(None)
    twelvepm= str(None)
    twopm= str(None)
    fourpm= str(None)
    sixpm= str(None)

    conn= sqlite3.connect("Database.db") #connect to the database, database must be in the same folder! 
    c= conn.cursor() #make using the cursor quicker to type out

    part1=str("Select customerID,session FROM Booking WHERE date = '") #set the beginning of the statement, to appear before the varible 
    part3= ("'")

    part2= str("' and time= '8:00' and Instructor = '") #set the next part, to appear after the varible
    exe= str(part1+date+part2+instructor+part3) #turn the first part of the statement, the varible and the last part into one large string
    c.execute(exe) #actually run the string, which has become a functioning sql statement 
    eightam= c.fetchall() #fetch the result and turn into varible 
    eightam= str(eightam) #turn varible into a string 

    part2= str("' and time= '10:00' and Instructor = '") #repeat for 10, 12, 2 etc 
    exe= str(part1+date+part2+instructor+part3)
    c.execute(exe)
    tenam= c.fetchone()
    tenam= str(tenam) 

    part2= str("' and time= '12:00' and Instructor = '")
    exe= str(part1+date+part2+instructor+part3)
    c.execute(exe)
    twelvepm= c.fetchone()
    twelvepm= str(twelvepm)

    part2= str("' and time= '14:00' and Instructor = '")
    exe= str(part1+date+part2+instructor+part3)
    c.execute(exe)
    twopm= c.fetchone()
    twopm= str(twopm)

    part2= str("' and time= '16:00' and Instructor = '")
    exe= str(part1+date+part2+instructor+part3)
    c.execute(exe)
    fourpm= c.fetchone()
    fourpm= str(fourpm)

    part2= str("' and time= '18:00' and Instructor = '")
    exe= str(part1+date+part2+instructor+part3)
    c.execute(exe)
    sixpm= c.fetchone()
    sixpm= str(sixpm) 
    
    result=("8am:"+ eightam+ "\n"+ "10am:"+ tenam+ "\n"+ "12pm:"+ twelvepm+ "\n"+ "2pm:"+ twopm+ "\n"+ "4pm:"+ fourpm+ "\n"+ "6pm:"+ sixpm) #turn result into one paragraph string
    return(result)

def printTimeTable(infile):
    """takes a timetable output, and turns it into a graphical interface item"""
    import tkinter as tk #Savers new call to the module requiring full name
    window = tk.Tk() #makes the window
    window.resizable (0, 0) #disables resizing
    text= tk.Label(window, text= infile, justify= tk.LEFT, font=("Calibri", 12)) #makes text
    text.pack() #puts text in the window 
    window.mainloop() #runs the window 

    
if __name__ == "__main__": #stops testing happening when executed elsewhere
    Test= MaketimetableI("1/1/2018", "4")
    Test2= printTimeTable(Test)

