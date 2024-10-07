class date : 
    ngay='0'
    thang='00'
    nam ='0000'

    def __init__(self,ngay ,thang , nam ):
        self.ngay=ngay 
        self.thang=thang 
        self.nam = nam 

    def dislay (self ): 
        print ('ngay da nhap la : ', str(self.ngay)+'-'+str(self.thang)+'-'+str(self.nam))

    def next(self ): 
      thang31 = [ 1,3,5,7,8,10,12]
      thang30=[4,6,9,11]
      if self.thang in thang31 :
         if self.ngay <31:
            self.ngay=self.ngay+1 
         else :
            self.ngay=1 
            if self.thang==12 :
                self.thang=1 
                self.nam=self.nam+1
            else : 
                self.thang=self.thang+1  
      if self.thang in thang30:
         if self.ngay <30:
            self.ngay=self.ngay+1 
         else :
            self.ngay=1 
            self.thang=self.thang+1 

      if self.thang==2 and (self.nam %4 ==0 or self.nam%400==0) :
          
         if self.ngay <29:
            self.ngay=self.ngay+1 
         else :
            self.ngay=1 
            self.thang=self.thang+1 
      if self.thang==2 and (self.nam %4 !=0 ):
        if self.ngay <28:
            self.ngay=self.ngay+1 
        else :
            self.ngay=1 
            self.thang=self.thang+1 
      print ('ngay tiep theo  : ', str(self.ngay)+'-'+str(self.thang)+'-'+str(self.nam))
obj1=date(29,2,1600)
obj1.dislay()
obj1.next()