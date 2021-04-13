create table BenhNhan
(
IDbenhnhan int identity (1,1) primary key,
Ten nvarchar(50) ,
NamSinh int,
GioiTinh varchar(10),
Sdt varchar(10),
DiaChi nvarchar(50),
Note nvarchar(500),
Benh nvarchar(50)
)
select * from BenhNhan
create table ChucVu
(
IDchucvu int identity (1,1) primary key,
Name nvarchar(50) 

)
create table Users
(
IDUser int identity (1,1) primary key,
Name nvarchar(50) ,
[Password] nvarchar(50),
IDchucvu int,
foreign key (IDchucvu) references ChucVu(IDchucvu)

)
create table MucDo
(
IDmucdo int primary key,
Name nvarchar(50) ,
Number int
)

create table TrieuChung
(
IDtrieuchung int primary key,
Name nvarchar(100) ,
IDmucdo int,
foreign key (IDmucdo) references MucDo(IDmucdo)
)