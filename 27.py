# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:36:44 2024

@author: 苏清影
"""
# importing packages and modules
import numpy as np
import pandas as pd
import openpyxl  # 使用pd.read_excel中需要保证openpyxl库已安装，但可以不导入。

from numpy.linalg import inv  # 矩阵求逆
from numpy import dot  # 矩阵点乘
import matplotlib.pyplot as plt


from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm
import matplotlib.pyplot as plt

data26 = pd.read_excel(r'C:\Users\苏清影\Desktop\daa\26.xlsx',header = None)
data = np.array(data26)
y= data[:,2]
x10= data[:,0]
x1 = np.square(x10)

x2= data[:,1]
x = np.vstack((x1,x2))
x = x.T
m=np.zeros((31,1))
m.fill(1)
x = np.hstack((m,x))

def y_hat(a,x1,x2):
    x = np.vstack((x1,x2))
    x = x.T
    m=np.zeros((31,1))
    m.fill(1)
    x = np.hstack((m,x))
    y = dot(x,a)
    return y

#beta最小二乘估计
beta = dot(dot(inv(np.dot(x.T,x)), x.T), y.T) 

H = dot(x,dot(inv(np.dot(x.T,x)), x.T)) 
I = np.eye(31)
#sigma无偏估计
sigma =  dot(y.T , dot(I-H , y)) *(1/28)

y_hat(beta,x1,x2)
cha = y-y_hat(beta,x1,x2)
#学生化残差
r=np.zeros((31,1))
for i in range(0,30):
    r[i]=cha[i]/(np.sqrt(sigma)*np.sqrt(H[i][i]))

fig = sm.qqplot(r, line='45')

transformed_data, best_lambda = boxcox(y)
#beta最小二乘估计
beta2 = dot(dot(inv(np.dot(x.T,x)), x.T), transformed_data.T) 

H = dot(x,dot(inv(np.dot(x.T,x)), x.T)) 
I = np.eye(31)
#sigma无偏估计
sigma2 =  dot(y.T , dot(I-H , transformed_data)) *(1/28)


y_hat(beta,x1,x2)
cha2 = transformed_data-y_hat(beta,x1,x2)
#学生化残差
r=np.zeros((31,1))
for i in range(0,30):
    r[i]=cha[i]/(np.sqrt(sigma)*np.sqrt(H[i][i]))
    
fig = sm.qqplot(r, line='45')
