# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:58:17 2024

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
import statsmodels.formula.api as smf
from itertools import combinations
 


data29 = pd.read_excel(r'C:\Users\苏清影\Desktop\daa\29.xlsx',header = None)

data = np.array(data29)
y= data[:,3]
x1= data[:,0]
x2= data[:,1]
x3= data[:,2]
x = np.vstack((x1,x2,x3))
x = x.T
m=np.zeros((23,1))
m.fill(1)
x = np.hstack((m,x))

#beta最小二乘估计
beta = dot(dot(inv(np.dot(x.T,x)), x.T), y.T) 

H = dot(x,dot(inv(np.dot(x.T,x)), x.T)) 
I = np.eye(23)
#sigma无偏估计
sigma =  dot(y.T , dot(I-H , y)) *(1/19)
def y_hat(a,x1,x2,x3):
    x = np.vstack((x1,x2,x3))
    x = x.T
    m=np.zeros((23,1))
    m.fill(1)
    x = np.hstack((m,x))
    y = dot(x,a)
    return y

y_hat(beta,x1,x2,x3)
cha = y-y_hat(beta,x1,x2,x3)
#学生化残差
r=np.zeros((23,1))
for i in range(0,22):
    r[i]=cha[i]/(np.sqrt(sigma)*np.sqrt(H[i][i]))
    
fig = sm.qqplot(r, line='45')


 #残差准则
model = sm.OLS(y, x).fit()

print(model.summary())

#残差平方和
sse = np.sum ((model. fittedvalues - y ) ** 2)
#print(model.ssr)
ssr = np. sum ((model. fittedvalues - y. mean ()) ** 2)
sst = ssr + sse
mse =1-(22/19)*(sse/sst)


df = pd.read_csv("C:\\Users\\苏清影\\Desktop\\daa\\292.csv")

def allziji(df):
    
    list1 = [1,2,3]
    n = 23
    R2 = []
    names = []
    
    #找到所有子集，并依次循环
    for a in range(len(list1)+1):
        for b in combinations(list1,a+1):
            p = len(list(b))
 
            data1 = pd.concat([df.iloc[:,i-1] for i in list(b) ],axis = 1)#结合所需因子
            
            name = "y~"+("+".join(data1.columns))#组成公式
            
            data = pd.concat([df['y'],data1],axis=1)#结合自变量和因变量
            
            result = smf.ols(name,data=data).fit()#建模
            
            #计算R2a
            r2 = (n-1)/(n-p-1)
            r2 = r2 * (1-result.rsquared**2)
            r2 = 1 - r2
            
            R2.append(r2)
            names.append(name)
            
    finall = {"公式":names,
              "R2a":R2}
    data = pd.DataFrame(finall)
    
    print("""根据自由度调整复决定系数准则得到：
        最优子集回归模型为：{}；
        其R2a值为：{}""".format(data.iloc[data['R2a'].argmax(),0],data.iloc[data['R2a'].argmax(),1]))
    
    result = smf.ols(name,data=df).fit()#建模
    print()
    print(result.summary())



#cp准则
def cp(df,mse):
    
    list1 = [1,2,3]
    n = 23
    Cp = []
    names = []
    
    #找到所有子集，并依次循环
    for a in range(len(list1)+1):
        for b in combinations(list1,a+1):
            p = len(list(b))
 
            data1 = pd.concat([df.iloc[:,i-1] for i in list(b) ],axis = 1)#结合所需因子
            
            name = "y~"+("+".join(data1.columns))#组成公式
            
            data = pd.concat([df['y'],data1],axis=1)#结合自变量和因变量
            
            result = smf.ols(name,data=data).fit()#建模
            
            #计算cp
            sse = np.sum ((result. fittedvalues -df['y'] ) ** 2)
            
            cp =sse/mse -(n-p)
           
            
            Cp.append(cp)
            names.append(name)
            
    finall = {"公式":names,
              "Cp":Cp}
    data = pd.DataFrame(finall)
    
    print("""根据自由度调整复决定系数准则得到：
        最优子集回归模型为：{}；
        其Cp值为：{}""".format(data.iloc[data['Cp'].argmax(),0],data.iloc[data['Cp'].argmax(),1]))
    
    result = smf.ols(name,data=df).fit()#建模
    print()
    print(result.summary())
    
    

def zhubuhuigui(df):
    forward = [i for i in range(0,4)]#备选因子
    backward = []#备退因子
    ceshi = []#存放加入单个因子后的模型
    zhengshi = []#收集确定因子
    delete = []#被删因子
    
    while forward:
        forward_aic = []#前进aic
        backward_aic = []#后退aic
        
        for i in forward:
            ceshi = [j for j in zhengshi]
            ceshi.append(i)
            data1 = pd.concat([df.iloc[:,i] for i in ceshi ],axis = 1)#结合所需因子
            name = "y~"+("+".join(data1.columns))#组成公式
            data = pd.concat([df['y'],data1],axis=1)#结合自变量和因变量
            result = smf.ols(name,data=data).fit()#建模
            forward_aic.append(result.aic)#将所有aic存入
            
        for i in backward:
            if (len(backward)==1):
                pass
            
            else:
                ceshi = [j for j in zhengshi]
                ceshi.remove(i)            
                data1 = pd.concat([df.iloc[:,i] for i in ceshi ],axis = 1)#结合所需因子
                name = "y~"+("+".join(data1.columns))#组成公式
                data = pd.concat([df['y'],data1],axis=1)#结合自变量和因变量
                result = smf.ols(name,data=data).fit()#建模
                backward_aic.append(result.aic)#将所有aic存入
                
        if backward_aic:
            if forward_aic:
                c0 = min(min(backward_aic),min(forward_aic))
                
            else:
                c0 = min(backward_aic)
                
        else:
            c0 = min(forward_aic)
            
        if c0 in backward_aic:
            zhengshi.remove(backward[backward_aic.index(c0)])
            delete.append(backward_aic.index(c0))
            backward.remove(backward[delete[-1]])#删除已删因子
            forward.append(backward[delete[-1]])
            
        else:
            zhengshi.append(forward[forward_aic.index(c0)])#查找最小的aic并将最小的因子存入正式的模型列表当中
            forward.remove(zhengshi[-1])#删除已有因子
            backward.append(zhengshi[-1])
 
    name = "y~"+("+".join(data1.columns))#组成公式
    print("最优模型为：{}，其aic为：{}".format(name,c0))
    result = smf.ols(name,data=data).fit()#建模
    print()
    print(result.summary())


zhubuhuigui(df)

# [1] 9.122225
