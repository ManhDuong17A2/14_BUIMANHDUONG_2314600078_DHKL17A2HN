class ps : 
    tuso=None 
    mauso=None
    def __init__(self,tuso,mauso) :
        self.tuso=tuso
        self.mauso=mauso

    @classmethod 
    def ktra (self):
        if self.mauso=='0':
            print ('phan so khong hop le , mau so phai khac 0')
    @classmethod
    def nhapphanso(self):
        self.tuso=input('nhap tu so : ')
        self.mauso=input ('nhap mau so : ')
    
    @classmethod
    def inphanso(self): 
        if self.mauso!='0': 
         phanso =  self.tuso + '/'+ self.mauso
         print ( 'phan so duoc nhap la : ',phanso)

ps.nhapphanso()
ps.ktra()
ps.inphanso()

