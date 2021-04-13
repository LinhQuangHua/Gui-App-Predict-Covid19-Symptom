import tkinter
from tkinter import messagebox  
from tkinter import *
from PIL import Image,ImageTk
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QUANGKUN\LINHQUANG;'
                      'Database=Demo_CNPMNC;'
                      'Trusted_Connection=yes;')
#======================================
root = Tk()
root.geometry('500x500')
root.title("LOGIN")

imge=Image.open("Team Male.png")
photo=ImageTk.PhotoImage(imge)
lab=Label(image=photo)
lab.pack()

#logo
img = PhotoImage(file="doctor.png")
root.tk.call('wm', 'iconphoto', root._w, img)

label_0 = Label(root, text="LOGIN",relief="solid",width=20,font=("arial", 19,"bold"))
label_0.place(x=90,y=150)


label_1 = Label(root, text="Username :",width=20,font=("bold", 10))
label_1.place(x=80,y=240)

entry_1 = Entry(root)
entry_1.place(x=240,y=242)


label_2 = Label(root, text="Password :",width=20,font=("bold", 10))
label_2.place(x=80,y=280)

entry_2 = Entry(root, show='*')
entry_2.place(x=240,y=282)


l= Label(root,width=50, text='CẢ NƯỚC CÙNG CHUNG TAY CHỐNG COVID-19')
l.place(x=70,y=330)
"""
label_4 = Label(root, text="Chuc vu :",width=20,font=("bold", 10))
label_4.place(x=95,y=320)

entry_checkbox = Entry(root)
def check01():
    l.config(text='Xin chào Trưởng khoa!')
    var2.set('No')
    var3.set('No')
    entry_checkbox = int(1)
    print(entry_checkbox)
    
def check02():
    l.config(text='Xin chào Bác Sĩ!')
    var1.set('No')
    var3.set('No')
    entry_checkbox = int(2)
    print(entry_checkbox)
    
def check03():
    l.config(text='Xin chào Y tá!')
    var2.set('No')
    var1.set('No')
    entry_checkbox = int(3)
    print(entry_checkbox)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

c1 = Checkbutton(root, text="Truong khoa",variable=var1,command=check01).place(x=230,y=320)  #check box 3
c2 = Checkbutton(root, text="Bac Si",variable=var2,command=check02).place(x=330,y=320)   #check box 1
c3 = Checkbutton(root, text="Y Ta",variable=var3,command=check03).place(x=400,y=320)  #check box 2
"""
#=========================================================
def check():
    if entry_1.get() == "":
        messagebox.showinfo("error","Please! Enter user name.")
    else:    
        root.destroy()
        import Demo_Doctor
    
def CheckLogin():
    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QUANGKUN\LINHQUANG;'
                      'Database=Demo_CNPMNC;')
    cursor = conn.cursor()
    find_user = ('SELECT * FROM Demo_CNPMNC.dbo.Users Where Name = ? and Password = ?')
    cursor.execute(find_user,[(entry_1.get()),(entry_2.get())])
    results = cursor.fetchall()
    if entry_1.get() == "" or entry_2.get() == "":
        messagebox.showinfo("error","Please! Enter user name and password.")
    elif results:
        root.destroy()
        import Doctor
    else:
        messagebox.showinfo("error","Please! Check your user and password.")
        
def openNurse():
    root.destroy()
    import Doctor
def close():
    root.destroy()
but_login=Button(root, text='Login',width=12,bg='brown',fg='white', command= CheckLogin).place(x=130,y=380)
but_quit=Button(root, text='Quit',width=12,bg='brown',fg='white',command= close).place(x=280,y=380)

root.mainloop()
