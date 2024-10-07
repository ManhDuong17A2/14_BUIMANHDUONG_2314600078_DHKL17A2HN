class tamgiac : 
    def __init__(self,a,b,c ):
        self.a=a 
        self.b=b
        self.c=c 

    def gioithieu (self):
        print ('tam giac la hinh tao boi 3 dinh noi voi nhau taoj thanh da giac kin ')


class tamgiacvuong(tamgiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def kiemtratamgiacvuong(self):
        if self.a**2==self.b**2 + self.c**2 or self.b**2==self.a**2 + self.c**2 or self.c**2==self.b**2 + self.a**2:
            print ('day la tam giac vuong ')


class tamgiaccan(tamgiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def ktratamgiaccan(self):
        if self.a==self.b or self.a==self.c or self.b==self.c : 
            print ('day la tam giac can ')

class tamgacdeu (tamgiaccan):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def ktratamgiacdeu(self):
        if self.a==self.b==self.c :
            print ('day la tma giac deu ')


obj1=tamgiac(2,3,4)
obj2=tamgiacvuong(3,4,5)
obj2.kiemtratamgiacvuong()
obj3=tamgiaccan(2,2,3)
obj3.ktratamgiaccan()
obj4=tamgacdeu(4,4,4)
obj4.ktratamgiacdeu()