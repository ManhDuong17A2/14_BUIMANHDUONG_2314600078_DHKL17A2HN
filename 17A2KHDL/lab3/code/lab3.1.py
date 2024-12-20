import pandas as pd 
import numpy as np 
import csv 

stock1=[]
path_stock1 = "D:\\LAPTRINH PYTHON\\Python_nangcao_BuiManhDuong_DHKL17A2HN\\17A2KHDL\\lab3\\data\\stocks1.csv"
with open (path_stock1, 'r',encoding='utf-8' ) as file_stock1 :
     dulieu_stock1= csv.reader ( file_stock1)
     for i in dulieu_stock1: 
          stock1.append(i)
          print (i)

print (stock1)

numpy_stock1 = np.array(stock1)
df
     
                                