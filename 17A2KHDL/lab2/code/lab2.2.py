import csv 
import numpy as np
path= "D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab2\\data\\diem_hoc_phan.csv"
data=[]
with open (path,'r',encoding='utf-8')as file :
    read= csv.reader(file)
    for row  in read :
        data.append(row[2:])
print (data[:5])
#chuyenr thanh mang numpy 
diemnumpyarray=np.array(data)
print(diemnumpyarray)
def chuyen_diem_hp(diem):
    if float (diem)<4 :
        return 'F'
    if 4<=float (diem)<5 :
        return "D"
    if 5<=float (diem) <6 :
        return 'C'
    if 6<=float (diem)<8:
        return 'B'
    if 8<=float (diem)<=10:
        return 'A'

dulieudiemchu=np.vectorize(chuyen_diem_hp)
diemchu=dulieudiemchu(diemnumpyarray[1:,:])
print (diemchu)