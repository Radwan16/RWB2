import sqlite3
import webbrowser
import tkinter as t
from tkinter import ttk, Frame
import os

db= sqlite3.connect("C:\Python\projekty_py\RWB2\data.db")
cursor = db.cursor()
class Info():
    def __init__(self,text,text2):
        self.text = text
        self.text2 = text2
        t.Label(tab1, text=text).place(relx=0.5,rely=1, anchor="s")
        t.Label(tab3, text=text).place(relx=0.5,rely=1, anchor="s")
        t.Label(tab2, text=text2).place(relx=0.5,rely=1, anchor="s")

def delete_entry(entry):
    entry.delete(0,'end')
def delete_add(entry,entry2):
    entry.delete(0,'end')
    entry2.delete(0,'end')

def open():
    try:
        link_id = id.get()
        query2 = f"SELECT Link FROM Score WHERE ID == ? ;"
        cursor.execute(query2,(link_id))
        link = cursor.fetchone()
        if link:
            webbrowser.open(link[0])
            delete_entry(id)
    except sqlite3.ProgrammingError:
        error = t.Label(tab1,text="Podaj ID")
        error.place(relx=0.5, rely=0.8, anchor="s")
        window.after(3000,lambda: error.destroy())
def add():
    global nazwa_entry
    global link_entry
    nazwa = nazwa_entry.get()
    link = link_entry.get()
    query3 = f"INSERT INTO Score VALUES(NULL, '{nazwa}', '{link}');"
    cursor.execute(query3)
    if nazwa and link:
        delete_add(nazwa_entry,link_entry)
    label1 = t.Label(tab2,text="Pomyślnie dodano! Uruchom ponownie program")
    label1.place(relx=0.5, rely=1, anchor="s")
    window.after(7000, lambda: label1.destroy())
def delete():
        del_id = del_score.get()
        query4 = f"DELETE FROM Score WHERE ID == ?;"
        cursor.execute(query4,(del_id,))
        if del_id:
            delete_entry(del_score)
            label2 = t.Label(tab3, text="Pomyślnie usunięto! Uruchom ponownie program")
            label2.place(relx=0.5, rely=1, anchor="s")
        else:
            error=t.Label(tab3,text="Podaj ID")
            error.place(relx=0.5, rely=0.8, anchor="s")
            window.after(3000, lambda: error.destroy())


window = t.Tk()
window.geometry("400x230")
window.title("RWB2")
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1, text="Open")
notebook.add(tab2, text="Add")
notebook.add(tab3, text="Delete")
notebook.pack(expand=True,fill="both")
Info("Wprowadź identyfikator","Wprowadź nazwę odnośnika oraz link")
def show(note, note2):
    query = "SELECT ID, Nazwa From Score"
    cursor.execute(query)
    rows = cursor.fetchall()
    for r in rows:
        t.Label(note, text=r).pack()
        t.Label(note2,text=r).pack()
show(tab1,tab3)
#Open webbrowser
id = t.Entry(tab1, width=5, justify="center")
id.pack()
t.Button(tab1, text="Open", command=open).pack()
#Add records
t.Label(tab2, text="Nazwa").place(relx=0.3, rely=0, anchor="n")
t.Label(tab2, text="Link").place(relx=0.7, rely=0, anchor="n")
nazwa_entry = t.Entry(tab2, width=6)
nazwa_entry.place(relx=0.3, rely=0.1,anchor="n")
link_entry = t.Entry(tab2, width=10)
link_entry.place(relx=0.7, rely=0.1,anchor="n")
t.Button(tab2, text="Add", command=add).place(relx=0.5, rely=0.6, anchor="s")
# Delete records
del_score = t.Entry(tab3, width=5, justify="center")
del_score.pack()
t.Button(tab3, text="Delete", command=delete).pack()
window.mainloop()
db.commit()
db.close()