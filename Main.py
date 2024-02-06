import sqlite3
import webbrowser
import tkinter as t
from tkinter import ttk, Frame
db= sqlite3.connect("data.db")
cursor = db.cursor()
query = "SELECT ID, Nazwa FROM Score"
class Info():
    def info_tab1():
        t.Label(tab1,text="Wprowadź Identyfikator !").place(relx=0.5,rely=1,anchor="s")
    def info_tab3():
        t.Label(tab3,text="Wprowadź Identyfikator !").place(relx=0.5,rely=1,anchor="s")
def open():
    link_id = id.get()
    query2 = f"SELECT Link FROM Score WHERE ID == ? ;"
    cursor.execute(query2,(link_id))
    link = cursor.fetchone()
    webbrowser.open(link[0])
def add():
    global nazwa
    global link
    nazwa = nazwa.get()
    link = link.get()
    query3 = f"INSERT INTO Score VALUES(NULL, '{nazwa}', '{link}');"
    cursor.execute(query3)
    label1 = t.Label(tab2,text="Pomyślnie dodano! Uruchom ponownie program")
    label1.place(relx=0.5, rely=1, anchor="s")
    window.after(7000, lambda: label1.destroy())
def delete():
    del_id = del_score.get()
    query4 = f"DELETE FROM Score WHERE ID == ?;"
    cursor.execute(query4,(del_id))
    label2 = t.Label(tab3, text="Pomyślnie usunięto! Uruchom ponownie program")
    label2.place(relx=0.5, rely=1, anchor="s")
    window.after(7000, lambda: label2.destroy())
cursor.execute(query)
rows = cursor.fetchall()
window = t.Tk()
window.geometry("400x200")
window.title("RWB2")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1, text="Open")
notebook.add(tab2, text="Add")
notebook.add(tab3, text="Delete")
notebook.pack(expand=True,fill="both")
#Open webbrowser
for r in rows:
    r = t.Label(tab1, text=r).pack()
id = t.Entry(tab1, width=5, justify="center")
id.pack()
t.Button(tab1, text="Open", command=open).pack()
Info.info_tab1()
#Add records
t.Label(tab2, text="Nazwa").place(relx=0.3, rely=0, anchor="n")
t.Label(tab2, text="Link").place(relx=0.7, rely=0, anchor="n")
nazwa = t.Entry(tab2, width=6)
nazwa.place(relx=0.3, rely=0.1,anchor="n")
link = t.Entry(tab2, width=10)
link.place(relx=0.7, rely=0.1,anchor="n")
t.Button(tab2, text="Add", command=add).place(relx=0.4, rely=0.3)
# Delete records
for row in rows:
    t. Label(tab3, text=row).pack()
del_score = t.Entry(tab3, width=5, justify="center")
del_score.pack()
t.Button(tab3, text="Delete", command=delete).pack()
Info.info_tab3()
window.mainloop()
db.commit()
db.close()