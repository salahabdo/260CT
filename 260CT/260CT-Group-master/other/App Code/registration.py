from tkinter import *
import sqlite3

connect = sqlite3.connect(sqlite_file)
c = connect.cursor()

sqlite_file = 'Database.db'

#Label fields to link with SQLite DB
fields = 'ID', 'Forename', 'Surname', 'Date of Birth (DD/MM/YYYY)', 'Customer Experience', 'Account Status' 



def fetch(entries):
    
    for entry in entries:
        field = entry[0]
        text = entry[1].get()
        print ('%s: "%s"' % (field, text))

def makeform(root, fields):

    entries = []
    for field in fields:
        row = Frame(root)
        label = Label(row, width=25, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side = TOP, fill = X, padx = 5, pady = 5)
        
        label.pack(side = LEFT)
        ent.pack(side = RIGHT, expand = YES, fill = X)
        entries.append((field, ent))

    return entries

if __name__ == '__main__':

    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch (e)))
    b1 = Button(root, text = 'Quit', command = root.quit)
    b1.pack(side = LEFT, padx = 5, pady= 5)

    b2 = Button(root, text = 'Submit', command = (lambda e=ents: fetch(e)))
    b2.pack (side = LEFT, padx=5, pady=5)

    root.mainloop()
