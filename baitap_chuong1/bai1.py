class hinhchunhat:
    chuvi=None 
    dientich= None
    def __init__(self,chieudai , chieurong ):
        self.chieudai=chieudai
        self.chieurong=chieurong
        self.chuvi=None 
        self.dientich= None 

    @classmethod
    def nhapthongtin (self):
        self.chieudai=int (input('nhap chieu dai : '))
        self.chieurong=int (input('nhap chieu rong : '))
    @classmethod
    def tinhchuvi (self):
        self.chuvi= self.chieudai*2 + self.chieurong*2 
        print ('da tinh chu vi ')
    @classmethod
    def tinhdientich (self):
        self.dientich= self.chieudai * self.chieurong
        print ('da tinh dien tich')
    @classmethod    
    def inthongtin (self):
        print ('chieu dai la :',self.chieudai)
        print ('chieu rong la : ',self.chieurong)
        print ('chu vi la : ', self.chuvi)
        print ('dien tich la : ',self.dientich)


while True : 
    print ('1.nhap thong tin ')
    print ('2.tinh chu vi ')
    print ('3.tinh dien tich ')
    print ('4.inthong tin ')
    print ('5.exit ')
    choice = int( input ('nhap lua chon: '))

    if choice == 1 :
        hinhchunhat.nhapthongtin()
    if choice==2 :
        hinhchunhat.tinhchuvi()
    if choice==3 :
        hinhchunhat.tinhdientich()
    if choice==4 :
        hinhchunhat.inthongtin()
    if choice==5 :
        break 


