import pandas as pd
import plotly.express as px
import math

df=pd.read_csv('D:\MRUDULA KORE\MRUDULA\Python\Projects\STDEV_105\CSV\data_STDEV.csv',names=['data'])

print(df['data'])
data=df['data'].tolist()

n1=len('data')
sum=0

for i in data:
   sum=sum+i

mean=sum/n1
print('Mean of given data is :'+str(mean))


diff_list=[]
for i in data:
  diff_list.append(i-mean)

squared_list=[]
for i in diff_list:
  squared_list.append(i**2)

sum=0
for i in squared_list:
  sum=sum+i

temp=sum/(n1-1) 
stdev=math.sqrt(temp)
print('stdev of given data is='+str(stdev))

