class employee : 
    ngaysinh='0'
    thangsinh='00'
    namsinh ='0000'
    sinhnhat=None 

    ngayvao=None 
    thangvao=None 
    namvao=None 
    ngayvaocongty=None 

    hoten = None 
    def __init__(self,hoten,ngaysinh ,thangsinh , namsinh ):
        self.hoten=hoten
        self.ngaysinh=ngaysinh 
        self.thangsinh=thangsinh 
        self.namsinh = namsinh 
        self.sinhnhat=str(self.ngaysinh)+'-'+str(self.thangsinh)+'-'+str(self.namsinh)
       

    def ngayvaocty(self,ngayvao , thangvao , namvao ):
        self.ngayvao = ngayvao
        self.thangvao=thangvao
        self.namvao=namvao
        self.ngayvaocongty=str(self.ngayvao)+'-'+str(self.thangvao)+'-'+str(self.namvao)



danhsachnhanvien =[]
while True : 
 print ('1.nhap thong tin ')
 print ('2.xoa thong tin ')
 print ('3.lay thong tin ')
 print ('4.chinhsuathongtin ')
 print ('5.in danh sach nhan vien')
 print ('6.exit')
 choice=int (input('nhap lua chon : '))
 if choice==1: 
    a=input ('nhap ho ten : ')
    b=input ('nhap ngay sinh : ')
    c=input ('nhap thang sinh : ')
    d=input ('nhap nam sinh : ')
    obj1=employee(a,b,c,d)
    b1=input ('nhap ngay vao  : ')
    c1=input ('nhap thang vao : ')
    d1=input ('nhap nam vao : ')
    obj1.ngayvaocty(b1,c1,d1)
    danhsachnhanvien.append({'ho ten':obj1.hoten,
                             'sinh nhat':obj1.sinhnhat,
                             'ngay vao ':obj1.ngayvaocongty})
    

 if choice ==2 :
    snnguoixoa = input ('nhap ngay sinh nguoi muon xoa  :  ')
    tennguoixoa=input ('nhap ten nguoi muon xoa:  ')
    for i in danhsachnhanvien:
       if i['ho ten'] ==tennguoixoa and i['sinh nhat']==snnguoixoa:
          danhsachnhanvien.remove(i)

 if choice==3 : 
    snnguoilay = input ('nhap ngay sinh nguoi muon lay thong tin   :  ')
    tennguoilay=input ('nhap ten nguoi muon lay thong tin :  ')
    for i in danhsachnhanvien:
       if i['ho ten'] ==tennguoilay and i['sinh nhat']==snnguoilay:
          print (i)


 if choice==4 :
    snnguoithaydoi = input ('nhap ngay sinh nguoi muon xoa  :  ')
    tennguoithaydoi=input ('nhap ten nguoi muon xoa:  ')
    tenmoi = input ('nhap ten moi(neu khong thay doi thi nhap phim 0 ) ')
    snhatmoi= input ('nhap sinh nhat moi (neu khong thay doi nhap phim 0 ) : ')
    ngayvaolammoi = input('nhap ngay vao lam moi (neu khong thay doi nhap phim 0 ) ')
    
    for i in danhsachnhanvien:
       if i['ho ten'] ==tennguoithaydoi and i['sinh nhat']==snnguoithaydoi:
          if tenmoi !='0' : 
             i['ho ten']=tenmoi
          if snhatmoi!='0' :
             i['sinh nhat']=snhatmoi
          if ngayvaolammoi !='0' :
             i['ngay vao']=ngayvaolammoi
 if choice==5: 
    print (danhsachnhanvien)


 if choice == 6 : 
    break 
 



     

    
    
