import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QUANGKUN\LINHQUANG;'
                      'Database=Demo_CNPMNC;'
                      'Trusted_Connection=yes;')
def readMucDo(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute('SELECT Name,Number FROM Demo_CNPMNC.dbo.MucDo')
    data =[]
    for row in cursor:
        data.append(row[0])
    return data
    print(data)
    
##def benhnhan():
##    print("Danh sach benh nhan:")
##    conn = pyodbc.connect('Driver={SQL Server};'
##                      'Server=QUANGKUN\SQLEXPRESS;'
##                      'Database=Demo_CNPMNC;'
##                      'Trusted_Connection=yes;')
##    cursor = conn.cursor()
##    cursor.execute('SELECT * FROM Demo_CNPMNC.dbo.BenhNhan')
##    for row in cursor:
##        print(row)
##    print()

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
    ten = entry_2.get()
    namsinh= entry_3.get()
    sdt = entry_5.get() 
    diachi = entry_6.get()
    note = entry_7.get()
    benh = x    
    cursor = conn.cursor()
    cursor.execute(
        'insert into Demo_CNPMNC.dbo.BenhNhan(Ten,NamSinh,GioiTinh,Sdt,DiaChi,Note,Benh) values(?,?,?,?,?,?,?);',
        (ten,namsinh,gender,sdt,diachi,note,benh)                  

    )
    conn.commit()
    print("Resigter Successful!")

def logout():
    root.destroy()
    import Demo_LoginPage

def reset():
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')
    entry_7.delete(0, 'end')
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
    label_4.configure(text="")
def ChuanDoan():
    import covid_19
    #===============
    p = chuyendoi(p)
    o = chuyendoi(q)
    i = chuyendoi(r)
    l = chuyendoi(e)
    k = chuyendoi(a)
    j = chuyendoi(d)
    m = chuyendoi(f)
    n = chuyendoi(g)
    b = chuyendoi(y)
    h = chuyendoi(n)
    x = covid_19.Test(p,o,i,l,k,j,m,n,b,h)
    label_4.configure(text=x)
    AddBenhNhan(x)
    benhnhan
