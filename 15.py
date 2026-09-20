# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:40:25 2024

@author: 苏清影
"""


import numpy as np
import pandas as pd
import openpyxl  # 使用pd.read_excel中需要保证openpyxl库已安装，但可以不导入。
from scipy.stats import pearsonr
import seaborn as sns
import scipy.stats as stats
from scipy.stats import  t
import scipy
data15 = pd.read_excel(r'E:\Rcord\1.5.xlsx',header = None)
data = np.array(data15)
#1.5
meanv=np.mean(data,axis=0)
vari=np.cov(data,rowvar=False)
print("总体均值向量",meanv)
print("总体方差矩阵",vari)

#1.6
med_vect=np.median(data,axis=0)
num_vars = data.shape[1]
person_matrix = np.zeros((num_vars, num_vars))
#无显著性检验
person = data15.corr(method="pearson")

# 计算Spearman相关矩阵Q
spearman = data15.corr(method='spearman')

print("中位数向量M：", med_vect)
print("Person相关矩阵R：",person)
#print(person_matrix)
print("Spearman相关矩阵Q：")
print(spearman)

# 对R和Q的元素进行显著性检验
num_vars = data.shape[1]
person_ = np.array(person)
spearman_ = np.array(spearman)
p_values_R = np.zeros((num_vars, num_vars))
p_values_Q = np.zeros((num_vars, num_vars))
for i in range(num_vars):
    for j in range(num_vars):
        if i != j:
            # 计算样本量
            n = data.shape[0]
            # 计算t值
            t_value_R = person_[i, j] * np.sqrt((n - 2) / (1 - person_[i, j]**2))
            t_value_Q = spearman_[i, j] * np.sqrt((n - 2) / (1 - spearman_[i, j]**2))
            # 计算p值
            p_values_R[i, j] = t.sf(np.abs(t_value_R), n - 2) * 2  # 两尾检验
            p_values_Q[i, j] = t.sf(np.abs(t_value_Q), n - 2) * 2  # 两尾检验
            

# 输出相关矩阵和p值矩阵
print("Person相关矩阵R：")
print(person_)
print("Person相关矩阵R的p值：")
print(p_values_R)

print("Spearman相关矩阵Q：")
print(spearman_)
print("Spearman相关矩阵Q的p值：")
print(p_values_Q)




