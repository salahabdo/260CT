import tkinter as tk
import sys
import sqlite3

def checkBookingChris(): 
   window = tk.Tk()
   window.title('Please enter your reference number')
   window.geometry('450x300')

   tk.Label(window,text='search booking').place(x=50,y=120)

   var_ref_num = tk.StringVar()
   entry_ref_num = tk.Entry(window,textvariable=var_ref_num)
   entry_ref_num.place(x=160,y=120)

   def usr_enter():
      def usr_update():
         conn = sqlite3.connect('database.db')

         executeme= str("UPDATE Booking set checking = 'True' where Ref_number = "+ stringx) 
         conn.execute(executeme)
         conn.commit()

         cursor = conn.execute("SELECT * from Booking where Ref_number = "+stringx)
         result = []
         for row in cursor:
            result.append("Ref_number =  " + str(row[0]))
            result.append("customerID = " + str(row[1]))
            result.append("session = " + str(row[2]))
            result.append("date = " + str(row[3]))
            result.append("time = " + str(row[4]))
            result.append("checking = "+ str(row[5]))
            result.append("Instructor = "+ str(row[6]))
         window = tk.Tk()
         window.title('show the details')
         window.geometry('900x900')

         tk.Label(window,text=str(result)).place(x=10,y=120)
         tk.Label(window,text='update successful').place(x=10,y=140)

         conn.close()


      stringx = entry_ref_num.get() #x must be string or made into string at later point
      stringx = str(stringx)
      conn = sqlite3.connect('database.db')

      

      cursor = conn.execute("SELECT * from Booking where Ref_number = "+stringx)
      result = []
      for row in cursor:
         result.append("Ref_number =  " + str(row[0]))
         result.append("customerID = " + str(row[1]))
         result.append("session = " + str(row[2]))
         result.append("date = " + str(row[3]))
         result.append("time = " + str(row[4]))
         result.append("checking = "+ str(row[5]))
         result.append("Instructor = "+ str(row[6]))
      window = tk.Tk()
      window.title('show the details')
      window.geometry('900x900')

      tk.Label(window,text=str(result)).place(x=10,y=120)
      btn_confirm = tk.Button(window,text='update?',command=usr_update)
      btn_confirm.place(x=150, y=170)
      conn.close()
      
   btn_enter = tk.Button(window,text='enter',command=usr_enter)
   btn_enter.place(x=150, y=170)
   window.mainloop()

