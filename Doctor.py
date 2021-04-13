import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QUANGKUN\LINHQUANG;'
                      'Database=Demo_CNPMNC;'
                      'Trusted_Connection=yes;')
from controller import readMucDo


def readMucDo(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute('SELECT Name,Number FROM Demo_CNPMNC.dbo.MucDo')
    data = []
    for row in cursor:
        data.append(row[0])
    return data
    print(data)


def benhnhan():
    print("Danh sach benh nhan:")
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=QUANGKUN\LINHQUANG;'
                          'Database=Demo_CNPMNC;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Demo_CNPMNC.dbo.BenhNhan')
    for row in cursor:
        print(row)
    print()


def chuyendoi(x):
    if x == 'Không':
        x = 0
    elif x == 'Hiếm':
        x = 1
    elif x == 'Đôi Khi':
        x = 2
    elif x == 'Vừa Phải':
        x = 3
    elif x == 'Phổ Biến':
        x = 4
    return x


def AddBenhNhan(x):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=QUANGKUN\LINHQUANG;'
                          'Database=Demo_CNPMNC;'
                          'Trusted_Connection=yes;')
    if c41_v1.set('Yes'):
        gender = 'Nam'
    else:
        gender = 'Nu'
    ten = entry_222.get()
    namsinh = entry_333.get()
    sdt = entry_555.get()
    diachi = entry_666.get()
    note = entry_777.get()
    benh = x
    cursor = conn.cursor()
    cursor.execute(
        'insert into Demo_CNPMNC.dbo.BenhNhan(Ten,NamSinh,GioiTinh,Sdt,DiaChi,Note,Benh) values(?,?,?,?,?,?,?);',
        (ten, namsinh, gender, sdt, diachi, note, benh)

    )
    conn.commit()
    print("Resigter Successful!")


def logout():
    root.destroy()
    import Demo_LoginPage


def reset():
    entry_222.delete(0, 'end')
    entry_333.delete(0, 'end')
    entry_555.delete(0, 'end')
    entry_666.delete(0, 'end')
    entry_777.delete(0, 'end')
    combo_8.set('')
    combo_9.set('')
    combo_10.set('')
    combo_11.set('')
    combo_12.set('')
    combo_13.set('')
    combo_14.set('')
    combo_15.set('')
    combo_16.set('')
    combo_17.set('')
    c41_v1.set('No')
    c42_v2.set('No')
    label_result.configure(text="")


def ChuanDoan():
    import covid_19
    # ===============
    p = chuyendoi(combo_8.get())
    o = chuyendoi(combo_9.get())
    i = chuyendoi(combo_10.get())
    l = chuyendoi(combo_11.get())
    k = chuyendoi(combo_12.get())
    j = chuyendoi(combo_13.get())
    m = chuyendoi(combo_14.get())
    n = chuyendoi(combo_15.get())
    b = chuyendoi(combo_16.get())
    h = chuyendoi(combo_17.get())
    x, y = covid_19.Test(p, o, i, l, k, j, m, n, b, h)  # x la chuan doan, y la ti le %
    label_result.configure(text=x)
    label_tile.configure(text=y)
    AddBenhNhan(x)
    benhnhan


# =================================================
# intializing the window
root = tk.Tk()
root.title("Bác Sĩ")
# Size of the window 
root.geometry('1100x700')
# Create Tab Control
TAB_CONTROL = ttk.Notebook(root)

# Tab1=======================================================================
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Chuẩn Đoán')
# ttk.Label(TAB1, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)

label_0 = ttk.Label(TAB1, text="CHUẨN ĐOÁN NHANH COVID-19", relief="solid", width=28, font=("arial", 19, "bold"))
label_0.place(x=350, y=50)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
label_1 = ttk.Label(TAB1, text="THÔNG TIN BỆNH NHÂN", width=25, font=("bold", 15))
label_1.place(x=90, y=120)

label_2 = ttk.Label(TAB1, text="Họ và tên :", width=20, font=("bold", 10))
label_2.place(x=50, y=170)
entry_222 = ttk.Entry(TAB1, width=30)  # textbox
entry_222.place(x=120, y=170)

label_3 = ttk.Label(TAB1, text="Năm sinh :", width=20, font=("bold", 10))
label_3.place(x=50, y=220)
entry_333 = ttk.Entry(TAB1, width=30)  # textbox
entry_333.place(x=120, y=220)

label_4 = ttk.Label(TAB1, text="Giới tính :", width=20, font=("bold", 10))
label_4.place(x=50, y=270)
c41_v1 = tk.StringVar()
c42_v2 = tk.StringVar()
c41 = ttk.Checkbutton(TAB1, text="Nam", variable=c41_v1).place(x=120, y=270)  # check box 1
c42 = ttk.Checkbutton(TAB1, text="Nữ", variable=c42_v2).place(x=200, y=270)  # check box 2
# c41_v1.set('No')
# c42_v2.set('No')

label_5 = ttk.Label(TAB1, text="SĐT :", width=20, font=("bold", 10))
label_5.place(x=50, y=320)
entry_555 = ttk.Entry(TAB1, width=30)  # textbox
entry_555.place(x=120, y=320)

label_6 = ttk.Label(TAB1, text="Địa chỉ :", width=20, font=("bold", 10))
label_6.place(x=50, y=370)
entry_666 = ttk.Entry(TAB1, width=30)  # textbox
entry_666.place(x=120, y=370)

label_7 = ttk.Label(TAB1, text="Ghi chú :", width=20, font=("bold", 10))
label_7.place(x=50, y=420)
entry_777 = ttk.Entry(TAB1, width=30)  # textbox
entry_777.place(x=120, y=420)

line = tk.Frame(root, height=400, width=7, bg="green").place(x=400, y=150)
# xxxxxxxxxxxxxxxxxxxxxxxxxxx
label_2 = ttk.Label(TAB1, text="TRIỆU CHỨNG", width=25, font=("bold", 15))
label_2.place(x=700, y=120)
# uuuuuuuuuuuuuuuuuuuuuuuuuuu
label_8 = ttk.Label(TAB1, text="Sốt :", width=20, font=("bold", 10))
label_8.place(x=500, y=170)
combo_8 = ttk.Combobox(TAB1)
combo_8['values'] = readMucDo(conn)
combo_8.current(0)  # set the selected item
combo_8.place(x=630, y=170)

label_9 = ttk.Label(TAB1, text="Ho Khan :", width=20, font=("bold", 10))
label_9.place(x=500, y=220)
combo_9 = ttk.Combobox(TAB1)
combo_9['values'] = readMucDo(conn)
combo_9.current(0)  # set the selected item
combo_9.place(x=630, y=220)

label_10 = ttk.Label(TAB1, text="Khó Thở :", width=20, font=("bold", 10))
label_10.place(x=500, y=270)
combo_10 = ttk.Combobox(TAB1)
combo_10['values'] = readMucDo(conn)
combo_10.current(0)  # set the selected item
combo_10.place(x=630, y=270)

label_11 = ttk.Label(TAB1, text="Đau Đầu :", width=20, font=("bold", 10))
label_11.place(x=500, y=320)
combo_11 = ttk.Combobox(TAB1)
combo_11['values'] = readMucDo(conn)
combo_11.current(0)  # set the selected item
combo_11.place(x=630, y=320)

label_12 = ttk.Label(TAB1, text="Đau Nhức Cơ Thể :", width=20, font=("bold", 10))
label_12.place(x=500, y=370)
combo_12 = ttk.Combobox(TAB1)
combo_12['values'] = readMucDo(conn)
combo_12.current(0)  # set the selected item
combo_12.place(x=630, y=370)

# uuuuuuuuuuuuuuuuuuuuuuuuuuu  
label_13 = ttk.Label(TAB1, text="Đau Họng :", width=20, font=("bold", 10))
label_13.place(x=800, y=170)
combo_13 = ttk.Combobox(TAB1)
combo_13['values'] = readMucDo(conn)
combo_13.current(0)  # set the selected item
combo_13.place(x=880, y=170)

label_14 = ttk.Label(TAB1, text="Mệt Mỏi :", width=20, font=("bold", 10))
label_14.place(x=800, y=220)
combo_14 = ttk.Combobox(TAB1)
combo_14['values'] = readMucDo(conn)
combo_14.current(0)  # set the selected item
combo_14.place(x=880, y=220)

label_15 = ttk.Label(TAB1, text="Tiêu Chảy :", width=20, font=("bold", 10))
label_15.place(x=800, y=270)
combo_15 = ttk.Combobox(TAB1)
combo_15['values'] = readMucDo(conn)
combo_15.current(0)  # set the selected item
combo_15.place(x=880, y=270)

label_16 = ttk.Label(TAB1, text="Sổ Mũi :", width=20, font=("bold", 10))
label_16.place(x=800, y=320)
combo_16 = ttk.Combobox(TAB1)
combo_16['values'] = readMucDo(conn)
combo_16.current(0)  # set the selected item
combo_16.place(x=880, y=320)

label_17 = ttk.Label(TAB1, text="Hắt Hơi :", width=20, font=("bold", 10))
label_17.place(x=800, y=370)
combo_17 = ttk.Combobox(TAB1)
combo_17['values'] = readMucDo(conn)
combo_17.current(0)  # set the selected item
combo_17.place(x=880, y=370)
# uuuuuuuuuuuuuuuuuuuuuuuuuuu
label_3 = ttk.Label(TAB1, text="Chuẩn Đoán  ==> ", width=25, font=("bold", 15))
label_3.place(x=630, y=480)
label_result = ttk.Label(TAB1, text="", width=15, font=("arial", 19, "bold"))
label_result.place(x=820, y=475)

label_tile = ttk.Label(TAB1, text="Tỉ lệ mắc bệnh  ==> ", width=25, font=("bold", 15))
label_tile.place(x=630, y=550)
label_tile = ttk.Label(TAB1, text="", width=15, font=("arial", 19, "bold"))
label_tile.place(x=820, y=545)

loginButton = ttk.Button(TAB1, text="Chuẩn Đoán", width=20, command=ChuanDoan).place(x=650, y=420)
loginButton = ttk.Button(TAB1, text="Reset", width=20, command=reset).place(x=850, y=420)
loginButton = ttk.Button(TAB1, text="Đăng Xuất", width=20, command=logout).place(x=850, y=600)

# Tab2=======================================================================
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Danh Sách Bệnh Nhân')


def deleteBN():
    print("Delete")
    tenbbb = entry_222.get()
    cursor = conn.cursor()
    cursor.execute(
        'delete from Demo_CNPMNC.dbo.BenhNhan where Ten = ?', (tenbbb)
    )
    conn.commit()
    messagebox.showinfo("Thông báo", "Delete Successful!")


label_0 = ttk.Label(TAB2, text="DANH SÁCH BỆNH NHÂN", relief="solid", width=22, font=("arial", 19, "bold"))
label_0.place(x=350, y=50)
# oooooooooooooooooooooooo
label_1 = ttk.Label(TAB2, text="THÔNG TIN BỆNH NHÂN", width=25, font=("bold", 15))
label_1.place(x=90, y=120)

label_2 = ttk.Label(TAB2, text="Họ và tên :", width=20, font=("bold", 10))
label_2.place(x=50, y=170)

x = tk.StringVar()
entry_2 = ttk.Entry(TAB2, width=30, textvariable=x)  # textbox
entry_2.place(x=120, y=170)

label_3 = ttk.Label(TAB2, text="Năm sinh :", width=20, font=("bold", 10))
label_3.place(x=50, y=220)
entry_3 = ttk.Entry(TAB2, width=30)  # textbox
entry_3.place(x=120, y=220)

label_4 = ttk.Label(TAB2, text="Giới tính :", width=20, font=("bold", 10))
label_4.place(x=50, y=270)
c4_1 = tk.StringVar()
c4_2 = tk.StringVar()
c41 = tk.Checkbutton(TAB2, text="Nam", variable=c4_1).place(x=120, y=270)  # check box 1
c42 = tk.Checkbutton(TAB2, text="Nữ", variable=c4_2).place(x=200, y=270)  # check box 2
c4_1.set('No')
c4_2.set('No')

label_5 = ttk.Label(TAB2, text="SĐT :", width=20, font=("bold", 10))
label_5.place(x=50, y=320)
entry_5 = ttk.Entry(TAB2, width=30)  # textbox
entry_5.place(x=120, y=320)

label_6 = ttk.Label(TAB2, text="Địa chỉ :", width=20, font=("bold", 10))
label_6.place(x=50, y=370)
entry_6 = ttk.Entry(TAB2, width=30)  # textbox
entry_6.place(x=120, y=370)

label_7 = ttk.Label(TAB2, text="Ghi chú :", width=20, font=("bold", 10))
label_7.place(x=50, y=420)
entry_7 = ttk.Entry(TAB2, width=30)  # textbox
entry_7.place(x=120, y=420)

EditButton = ttk.Button(TAB2, text="Chỉnh Sửa", width=20).place(x=70, y=480)
DeleteButton = ttk.Button(TAB2, text="Xóa", command=deleteBN, width=20).place(x=230, y=480)
# oooooooooooooooooooooooo
label_2 = ttk.Label(TAB2, text="DANH SÁCH BỆNH NHÂN", width=25, font=("bold", 15))
label_2.place(x=700, y=120)

label_tk = ttk.Label(TAB2, text="Tìm kiếm :", width=20, font=("bold", 10))
label_tk.place(x=550, y=170)
entry_tk = ttk.Entry(TAB2, width=30)  # textbox
entry_tk.place(x=620, y=170)


def clear():
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')
    entry_7.delete(0, 'end')
    c4_1.set('')
    c4_2.set('')


def selectItem(event):
    # item = tree.focus()
    clear()

    item = tree.item(tree.selection())['values']
    if item[2] == 'Nam':
        c4_2.set('Yes')
    else:
        c4_1.set('Yes')
    print('  '.join(str(v) for v in item))
    # print(item[3])
    entry_2.insert(0, item[0])
    entry_3.insert(0, item[1])
    entry_5.insert(0, item[3])
    entry_6.insert(0, item[4])
    entry_7.insert(0, item[5])


def searchyear():
    tree.delete(*tree.get_children())
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=QUANGKUN\LINHQUANG;'
                          'Database=Demo_CNPMNC;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Demo_CNPMNC.dbo.BenhNhan')
    for row in cursor:
        if entry_tk.get() == str(row[2]):
            # tree.delete(*tree.get_children())
            tree.insert('', 'end', text="", values=(row[1], row[2], row[3], row[4], row[5], row[7]))
            # tree.tag_configure(str(row[2]),background='green')
            print(row[2])
            continue
        else:
            continue

    else:
        entry_tk.delete(0, 'end')
        entry_tk.insert(0, str(""))


def loadlist():
    tree.delete(*tree.get_children())
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=QUANGKUN\LINHQUANG;'
                          'Database=Demo_CNPMNC;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Demo_CNPMNC.dbo.BenhNhan')
    for row in cursor:
        tree.insert('', 'end', text="", values=(row[1], row[2], row[3], row[4], row[5], row[7]))


tree = ttk.Treeview(TAB2)

vsb = ttk.Scrollbar(TAB2, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')

tree.configure(yscrollcommand=vsb.set)

tree["columns"] = ("six", "one", "two", "three", "four", "five")
tree.column("#0", width=0, minwidth=0, stretch=tk.NO)
tree.column("six", width=150, minwidth=170, stretch=tk.NO)
tree.column("one", width=70, minwidth=80)
tree.column("two", width=70, minwidth=80)
tree.column("three", width=100, minwidth=120)
tree.column("four", width=100, minwidth=120)
tree.column("five", width=150, minwidth=120)

tree.heading("six", text="Tên bệnh nhân", anchor=tk.W)
tree.heading("one", text="Năm sinh", anchor=tk.W)
tree.heading("two", text="Giới tính", anchor=tk.W)
tree.heading("three", text="SĐT", anchor=tk.W)
tree.heading("four", text="Địa chỉ", anchor=tk.W)
tree.heading("five", text="Bệnh", anchor=tk.W)

tree.bind('<<TreeviewSelect>>', selectItem)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QUANGKUN\LINHQUANG;'
                      'Database=Demo_CNPMNC;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Demo_CNPMNC.dbo.BenhNhan')
for row in cursor:
    tree.insert('', 'end', text="", values=(row[1], row[2], row[3], row[4], row[5], row[7]))

tree.place(x=450, y=220)

SearchButton = ttk.Button(TAB2, text="Tìm Kiếm", width=15, command=searchyear).place(x=820, y=168)
LoadButton = ttk.Button(TAB2, text="Load", width=15, command=loadlist).place(x=920, y=168)
# Tab3=======================================================================
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Tình Hình Dịch Bệnh')

label_0 = ttk.Label(TAB3, text="CẬP NHẬT TÌNH HÌNH COVID-19", relief="solid", width=28, font=("arial", 19, "bold"))
label_0.place(x=350, y=50)
# ====================================================================
label_1 = ttk.Label(TAB3, text="VIỆT NAM", width=40, font=("bold", 20))
label_1.place(x=150, y=150)

label_3 = ttk.Label(TAB3, text="SỐ CA NHIỄM", width=40, font=("bold", 15))
label_3.place(x=150, y=220)

label_4 = ttk.Label(TAB3, text="TỬ VONG", width=40, font=("bold", 15))
label_4.place(x=160, y=320)

label_5 = ttk.Label(TAB3, text="HỒI PHỤC", width=40, font=("bold", 15))
label_5.place(x=160, y=420)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk

import pandas as pd
import requests
from bs4 import BeautifulSoup

# def case():
page = requests.get('https://www.worldometers.info/coronavirus/country/viet-nam/')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='col-md-8')
item = week.find_all(id='maincounter-wrap')
items = week.find_all(class_='maincounter-number')
SoCaNhiem = items[0].find('span').get_text()
Chet = items[1].find('span').get_text()
PhucHoi = items[2].find('span').get_text()
print(SoCaNhiem)
print(Chet)
print(PhucHoi)

entry_case = ttk.Label(TAB3, text=SoCaNhiem, width=40, font=("bold", 15))
entry_case.place(x=190, y=270)

label_dead = ttk.Label(TAB3, text=Chet, width=40, font=("bold", 15))
label_dead.place(x=200, y=370)

label_cover = ttk.Label(TAB3, text=PhucHoi, width=40, font=("bold", 15))
label_cover.place(x=190, y=470)
# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk

# ====================================================================

label_2 = ttk.Label(TAB3, text="THẾ GIỚI", width=40, font=("bold", 20))
label_2.place(x=700, y=150)

label_33 = ttk.Label(TAB3, text="SỐ CA NHIỄM", width=40, font=("bold", 15))
label_33.place(x=700, y=220)

label_44 = ttk.Label(TAB3, text="TỬ VONG", width=40, font=("bold", 15))
label_44.place(x=720, y=320)

label_55 = ttk.Label(TAB3, text="HỒI PHỤC", width=40, font=("bold", 15))
label_55.place(x=720, y=420)

# kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
page_tg = requests.get('https://www.worldometers.info/coronavirus/?utm_campaign=homeAdUOA?Si')
soup_tg = BeautifulSoup(page_tg.content, 'html.parser')
week = soup_tg.find(class_='col-md-8')
item_tg = week.find_all(id='maincounter-wrap')
items_tg = week.find_all(class_='maincounter-number')
SoCaNhiem_tg = items_tg[0].find('span').get_text()
Chet_tg = items_tg[1].find('span').get_text()
PhucHoi_tg = items_tg[2].find('span').get_text()
print(SoCaNhiem_tg)
print(Chet_tg)
print(PhucHoi_tg)

entry_case = ttk.Label(TAB3, text=SoCaNhiem_tg, width=40, font=("bold", 15))
entry_case.place(x=720, y=270)

label_dead = ttk.Label(TAB3, text=Chet_tg, width=40, font=("bold", 15))
label_dead.place(x=730, y=370)

label_cover = ttk.Label(TAB3, text=PhucHoi_tg, width=40, font=("bold", 15))
label_cover.place(x=725, y=470)

# Calling Main()
TAB_CONTROL.pack(expand=1, fill="both")
root.mainloop()
