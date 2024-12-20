#1 . tạo dữ liệu mô phỏng
import random
import numpy as np 
nhietdo = np.round(np.random.uniform(0,40,size=30 ),2) 
print (nhietdo)
#nhiet do trung binh 
nhietdotb=nhietdo.mean()
print (nhietdotb)
#2 .phân tích xu hường nhiệt độ 
max=nhietdo.max()
min=nhietdo.min()
print (f'nhietdocaonhat {max}', f'nhietdothapnhat {min}')
daynhietdocaonhat=np.argmax(nhietdo)+1
daynhietdothapnhat=np.argmin(nhietdo)+1
print (daynhietdocaonhat,daynhietdothapnhat)

#su chenh lech nhiet do giua cacs ngay 
ngaytruoc = nhietdo[:-1]
ngaysau = nhietdo[1:]
nhietdochenh=ngaytruoc-ngaysau
print (nhietdochenh)
print (nhietdochenh.max())
