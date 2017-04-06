import tkinter as tk
import sys
import sqlite3

def checkBookingChris():
   window = tk.Tk()
   window.title('Please enter your want to search')
   window.geometry('450x300')
   window.focus_force()

   tk.Label(window,text='search for ref_number').place(x=20,y=120)
   tk.Label(window,text='search for CustomerID').place(x=20,y=150)

   var_ref_num = tk.StringVar()
   entry_ref_num = tk.Entry(window,textvariable=var_ref_num)
   entry_ref_num.place(x=170,y=120)
   var_cum_id = tk.StringVar()
   entry_cum_id = tk.Entry(window,textvariable=var_cum_id)
   entry_cum_id.place(x=170,y=150)

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

         yIndex = 120
         for item in result:
            tk.Label(window, text=item).place(x=10, y=yIndex)
            yIndex += 20

         tk.Label(window,text='update successful').place(x=10,y=140)

         conn.close()


      stringx = var_ref_num.get() #x must be string or made into string at later point
      stringy = var_cum_id.get()
      conn = sqlite3.connect('database.db')
      if (stringx != "" and stringy != ""):
         cursor = conn.execute("SELECT * from Booking where Ref_number = "+stringx+" and customerID = "+stringy)
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

         yIndex = 120
         for item in result:
            tk.Label(window, text=item).place(x=10, y=yIndex)
            yIndex += 20
         
         btn_confirm = tk.Button(window,text='update?',command=usr_update)
         btn_confirm.place(x=150, y=260)
         conn.close()
         
      elif (stringx != ""):
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

         yIndex = 120
         for item in result:
            tk.Label(window, text=item).place(x=10, y=yIndex)
            yIndex += 20
         
         btn_confirm = tk.Button(window,text='update?',command=usr_update)
         btn_confirm.place(x=150, y=260)
         conn.close()
         
      elif (stringy != ""):
         cursor = conn.execute("SELECT * from Booking where customerID = "+stringy)
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

         yIndex = 20
         counter = 0
         for item in result:
            if (counter == 7):
               tk.Label(window, text="").place(x=10, y=yIndex)
               yIndex += 20
               counter = 0
            tk.Label(window, text=item).place(x=10, y=yIndex)
            
            yIndex += 20
            counter += 1

         btn_confirm = tk.Button(window,text='update?',command=usr_update)
         btn_confirm.place(x=300, y=150)
         conn.close()
      

    
   btn_enter = tk.Button(window,text='enter',command=usr_enter)
   btn_enter.place(x=150, y=190)
   window.mainloop()


