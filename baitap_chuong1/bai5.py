class stack : 
    nganxep = []
    phantu = None 

    def __init__(self):
        self.nganxep=[]

    def __del__(self):
        print ("doi tuong da bi xoa ")

    def push ( self):
        while True :
            print ('1.nhap phan tu tiep ')
            print ('2.dung lai ')
            
            choice = int(input ('nhap lua chon :  '))
            if choice ==1  : 
                self.nganxep.append(input('nhap them phan tu : '))
            if choice == 2 :
                break 
    def pop (self ): 
        print ( ' phan tu dinh cua ngan xep la : ', self.nganxep[-1])
    
    def capphatmang (self ):
        self.phantu=int (input ("nhap so phan tu của mảng : "))

    def ktra ( self ): 
         if len(self.nganxep)> self.phantu:
              print(self.nganxep)
              print ( ' mang da day ')
    
    def count (self ): 
        print ( 'so phan tu trong mang la :  ',len ( self.nganxep))
              


obj = stack()
obj.capphatmang()
obj.push()
obj.pop()
obj.ktra()
obj.count()
