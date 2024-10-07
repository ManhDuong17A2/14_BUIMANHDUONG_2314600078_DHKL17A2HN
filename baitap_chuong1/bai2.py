class ts : 
    thongtin=[]
    tongdiem=None 
    def __init__(self,hoten , diemtoan , diemly , diemhoa ) :
        self.hoten =hoten
        self.diemtoan=diemtoan 
        self.diemly = diemly 
        self.diemhoa = diemhoa  

    @classmethod
    def nhapthongtin (self): 
        self.hoten =input ('nhap ho ten :')
        self.diemtoan=int (input ('nhap diem toan : ')) 
        self.diemly = int (input ("nhap diem ly : "))
        self.diemhoa = int (input ('nhap diem hoa : '))
        self.thongtin.append({'hoten ': self.hoten,
                              'diemtoan':self.diemtoan,
                              'diemly':self.diemly,
                              'diemhoa':self.diemhoa,
                              'tongdiem':ts.tinhtongdiem()})

    @classmethod 
    def inthongtin (self): 
        print ('ho ten thi sinh : ',self.hoten)
        print ('diem ly : ',self.diemly)
        print ('diem toan : ',self.diemtoan)
        print ('diem hoa : ',self.diemhoa)
    
    @classmethod
    def tinhtongdiem (self ):
        self.tongdiem = self.diemhoa + self.diemly + self.diemtoan
        print (' tong diem la : ',self.tongdiem)
        return self.tongdiem
      

diemchuan = 20 

while True : 
    print ('1.nhap thong tin thi sinh : ')
    print ('2.exit ')
    choice = int (input (" nhap lua chon : "))
    if choice== 1 : 
        ts.nhapthongtin()
        ts.inthongtin()
        ts.tinhtongdiem()
        
       
    if choice == 2 : 
       break 

danhsachtrungtuyen=ts.thongtin.copy()
for i in danhsachtrungtuyen:
    if i['tongdiem']<diemchuan:
        danhsachtrungtuyen.remove(i) 
danhsachchinhsua = sorted(danhsachtrungtuyen, key=lambda x: x['tongdiem'], reverse=True)

print (danhsachchinhsua)



