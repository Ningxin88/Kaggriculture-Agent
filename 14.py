# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:05:45 2024

@author: 苏清影
"""

import numpy as np
import pandas as pd
import openpyxl  # 使用pd.read_excel中需要保证openpyxl库已安装，但可以不导入。
import matplotlib.pyplot as plt

data14 = pd.read_excel(r'E:\Rcord\1.4.xlsx',header = None)
data = np.array(data14)
data1= data[:,1]
data2= data[:,2]
#均值
mean1 = np.mean(data1)
mean2 = np.mean(data2)
#方差
vari1 = np.var(data1)
vari2 = np.var(data2)
#标准差
std1   = np.std(data1)
std2   = np.std(data2)
#变异系数
bianyi1 = std1/mean1
bianyi2 = std1/mean2
#偏度
pian1 = np.mean((data1-mean1)**3)/std1**4
pian2 = np.mean((data2-mean2)**3)/std2**4
#蜂度
feng1 = np.mean((data1-mean1)**4)/std1**4
feng2 = np.mean((data2-mean2)**4)/std2**4
#中位数
med1 = np.percentile(data1,50)
med2 = np.percentile(data2,50)
#上四分位数
up1 = np.percentile(data1,75)
up2 = np.percentile(data2,75)
#下四分位数
down1 = np.percentile(data1,25)
down2 = np.percentile(data2,25)
#四分位极差
w1 = up1-down1
w2 = up2-down2
print("X1均值: ",mean1)
print("X1方差: ",vari1)
print("X1标准差: ",std1)
print("X1变异系数: ",bianyi1)
print("X1偏度: ",pian1)
print("X1峰度: ",feng1)
print("X1中位数: ",med1)
print("X1上四分位数: ",up1)
print("X1下四分位数: ",down1)
print("X1四分位极差: ",w1)
print("X2均值: ",mean2)
print("X2方差: ",vari2)
print("X2标准差: ",std2)
print("X2变异系数: ",bianyi2)
print("X2偏度: ",pian2)
print("X2峰度: ",feng2)
print("X2中位数: ",med2)
print("X2上四分位数: ",up2)
print("X2下四分位数: ",down2)
print("X2四分位极差: ",w2)

#绘制直方图
#plt.hist(data1,bins = 'auto',alpha = 0.7,label ='X1',color = 'blue',rwidth = 0.85)
#plt.hist(data2,bins = 'auto',alpha = 0.7,label ='X2',color = 'red',rwidth = 0.85)
plt.hist([data1,data2],bins=10,stacked=True)
plt.show

#绘制经验分布函数图
def ecdf(data):
    x = np.sort(data)
    y= np.arange(1,len(data)+1)/len(data)
    return x,y
    
x1,y1 = ecdf(data1)
x2,y2 = ecdf(data2)

plt.plot(x1,y1,marker = '.',linestyle='none',color='blue',label='X1')
plt.plot(x2,y2,marker = '.',linestyle='none',color='red',label='X2')
plt.show