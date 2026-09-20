# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:33:27 2024

@author: 苏清影
"""

import numpy as np
import pandas as pd
import openpyxl  # 使用pd.read_excel中需要保证openpyxl库已安装，但可以不导入。
from scipy.stats import pearsonr
import seaborn as sns
from scipy.stats import  t
from scipy.stats import ttest_ind

data17 = pd.read_excel(r'E:\Rcord\1.7.xlsx',header = None)
data = np.array(data17)


meanv=np.mean(data,axis=0)
medv = np.median(data,axis=0)

person = data17.corr(method="pearson")

# 计算Spearman相关矩阵Q
spearman = data17.corr(method='spearman')

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

# 对R和Q的元素进行显著性检验(t检验)
person_ = np.array(person)
spearman_ = np.array(spearman)
x = person_.ravel()
y = spearman_.ravel()


res = ttest_ind(x, y)

print("均值向量",meanv)
print("中位数向量",medv)
# 输出相关矩阵和p值矩阵
print("Person相关矩阵R：")
print(person_)
print("Person相关矩阵R的p值：")
print(p_values_R)

print("Spearman相关矩阵Q：")
print(spearman_)
print("Spearman相关矩阵Q的p值：")
print(p_values_Q)


print("相关性检验结果：",res)