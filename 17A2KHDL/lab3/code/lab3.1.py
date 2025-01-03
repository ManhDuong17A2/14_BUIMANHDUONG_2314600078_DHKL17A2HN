import pandas as pd 
import numpy as np 
import csv 

'''stock1=[]
path_stock1 = "D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab3\\data\\stocks1.csv"
with open (path_stock1, 'r',encoding='utf-8' ) as file_stock1 :
     dulieu_stock1= csv.reader ( file_stock1)
     for i in dulieu_stock1: 
          stock1.append(i)
   

print (stock1)

numpy_stock1 = np.array(stock1)

stock2 = []
path_stock2= "D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab3\\data\\stocks2.csv"
     
with open (path_stock2,'r',encoding='utf-8') as file : 
     read= csv.reader(file)
     for  i in read:
          stock2.append(i)

print(stock2)'''

#doc du lieuj stock1 , stock2 vaof data frame 
path_stock1 = "D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab3\\data\\stocks1.csv"
path_stock2="D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab3\\data\\stocks2.csv"
df_stock1= pd.read_csv(path_stock1)
df_stock2=pd.read_csv(path_stock2)
print (df_stock1)
print (df_stock2)
print (df_stock1[:5][:]) #hient hi 5 dong dau tien 
stock_df=pd.concat([df_stock1,df_stock2],ignore_index=True)
print (stock_df[:5][:])
print (stock_df.head())
stock_df.info() #thoong tin tong quan sau khi gop 
#tinh gia tri turng binh cho moi ngay 
gt_tb_mongay = stock_df.groupby('date')[['open','high','low','close']].mean()
print (gt_tb_mongay.head())
#thay the gia tri null o cot low 
low_thaythe = df_stock1['low'].mean()
df_stock1.fillna(low_thaythe,inplace=True)
high_thaythe = df_stock1['high'].mean()
df_stock1.fillna(high_thaythe,inplace=True)

print (df_stock1)

#kiem tra null 
kt_null=df_stock1.isnull().sum()
print ('--------------------------------------------------------------------------------------')

path_companies="D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab3\\data\\companies.csv"
df_companies=pd.read_csv(path_companies)
print (df_companies.head())
#ket hop hai bang voi du lieu chung la cot symbol 
df_kethop=pd.merge(stock_df,df_companies,how='inner',left_on='symbol',right_on='name')
print (df_kethop)
#tinh gt dong cua close tb 
close_tb = df_kethop['close'].mean()
print (close_tb)
df_kethop.head()

#muntiIndex 
df_kethop.set_index(['symbol','date'],inplace=True)
print (df_kethop)
print ('-------------------------------------------------------------------')
tb_machungkhoan=df_kethop.groupby(['symbol','date'])[['open','high','low','close']].mean()
tb_machungkhoan=tb_machungkhoan.sort_index()
print(tb_machungkhoan)


