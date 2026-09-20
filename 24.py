# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:21:17 2024

@author: 苏清影
"""
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


data24 = pd.read_excel(r'C:\Users\苏清影\Desktop\daa\24.xlsx',header = None)

data = np.array(data24)
y= data[:,2]
x1= data[:,0]
x2= data[:,1]
x = np.vstack((x1,x2))
x = x.T
m=np.zeros((15,1))
m.fill(1)
x = np.hstack((m,x))

#beta最小二乘估计
beta = dot(dot(inv(np.dot(x.T,x)), x.T), y.T) 

H = dot(x,dot(inv(np.dot(x.T,x)), x.T)) 
I = np.eye(15)
#sigma无偏估计
sigma =  dot(y.T , dot(I-H , y)) *(1/12)


#models = sm.OLS(y,x).fit()
#方差分析表
df = pd.DataFrame({'人数':x1, '收入':x2,  '销量':y})
model = ols('销量 ~ 人数 + 收入', df).fit()
anova_table=anova_lm(model)

model2 = sm.OLS(y,x).fit()
newx = [220,2500]
pred = model2.predict(newx)
pred = model.get_prediction(newx)
conf_int = pred.conf_int()  # 置信区间


model = sm.OLS(Y,X)
results = model.fit()
result.summary()
def y_hat(a,x1,x2):
    x = np.vstack((x1,x2))
    x = x.T
    m=np.zeros((15,1))
    m.fill(1)
    x = np.hstack((m,x))
    y = dot(x,a)
    return y

y_hat(beta,x1,x2)
cha = y-y_hat(beta,x1,x2)
#学生化残差
r=np.zeros((15,1))
for i in range(0,14):
    r[i]=cha[i]/(np.sqrt(sigma)*np.sqrt(H[i][i]))

fig = sm.qqplot(r, line='45')
