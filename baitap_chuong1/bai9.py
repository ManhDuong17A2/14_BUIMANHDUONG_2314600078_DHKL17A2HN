

class dagiac :
    canh=None 
    def __init__(self  ) :
        pass  
    def gioithieu (self ): 
        print('Đa giác có thể có bất kỳ số cạnh nào miễn là các cạnh đều thẳng và nối thành một hình kín.')

    
class hinhbinhhanh(dagiac):
    def __init__(self,  canhday ,canhben ,chieucao ):
        super().__init__()
        self.canhday=canhday
        self.canhben=canhben
        self.chieucao=chieucao
        
    def tinhchuvi(self): 
        self.chuvi = 2*(self.canhben+self.canhday)
        print ('chu vi hinh binh hanh la : ',self.chuvi)


    def tinhdientich(self):
        self.dientich = self.canhday*self.chieucao
        print ('dien tich hinh binh hanh la : ',self.dientich)


class hinhchunhat(hinhbinhhanh):
    def __init__(self,canhday,canhben ):
        super().__init__(canhday , canhben ,chieucao=None )
        
    def tinhchuvi(self): 
        self.chuvi = 2*(self.canhben+self.canhday)
        print ('chu vi hinh chu nha laf : ',self.chuvi)
    def tinhdientich(self):
        self.dientich = self.canhday*self.canhben 
        print ('dien tich hinh chu nhat la : ',self.dientich)

        

    

class hinhvuong (hinhchunhat):
    def __init__(self, canhday, canhben=None ):
        super().__init__(canhday, canhben)



    def tinhchuvi(self): 
        self.chuvi = 4*(self.canhday)
        print ('chu vi hinh vuong la : ',self.chuvi)


    def tinhdientich(self):
        self.dientich = self.canhday*self.canhday
        print ('dien tich hinh vuong la : ',self.dientich)

obj1=dagiac()
obj2=hinhbinhhanh(3,4,5)
obj2.tinhchuvi()
obj2.tinhdientich()
obj3=hinhchunhat(7,8)
obj3.tinhchuvi()
obj3.tinhdientich()
obj4=hinhvuong(5)
obj4.tinhchuvi()
obj4.tinhdientich()
