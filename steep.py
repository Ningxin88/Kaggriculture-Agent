import numpy as np

#目标函数定义
def f1(x):
    return 0.5*x[0]**2 + 4.5*x[1]**2
def f2(x):
    return 0.5*x[0]**2 + 5000*x[1]**2

#函数梯度定义
def grad1(x):
    return np.array([x[0], 9*x[1]])
def grad2(x):
    return np.array([x[0], 10000*x[1]])

#Armijo线性搜索算法
def Armijo1(x, pk, c1=0.1, beta=0.5):
    alpha = 1
    while f1(x+alpha*pk) > f1(x) + c1*alpha*np.dot(grad1(x), pk):
        alpha *= beta
    return alpha

def Armijo2(x, pk, c1=0.1, beta=0.5):
    alpha = 1
    while f2(x+alpha*pk) > f2(x) + c1*alpha*np.dot(grad1(x), pk):
        alpha *= beta
    return alpha

#最速下降法
#max_iter为最大步数， tol为精度，要求更高精度时可更改
def steepest1(x0, max_iter=10000, tol=1e-6):
    x = x0
    k = 0
    while k < max_iter:
        g = grad1(x)
        d = -g
        alpha = Armijo1(x, d)
        x_new = x + alpha*d
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
        k += 1
    return x, f1(x), k

def steepest2(x0, max_iter=10000, tol=1e-6):
    x = x0
    k = 0
    while k < max_iter:
        g = grad2(x)
        d = -g
        alpha = Armijo2(x, d)
        x_new = x + alpha*d
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new
        k += 1
    return x, f2(x), k

# 测试
x0 = np.array([1, 1])
x1_star, f1_min, k1 = steepest1(x0)
print("第一个函数最优解为：", x1_star)
print("该目标函数的最小值为：", f1_min)
print("第一个函数第几次结束：", k1)

x2_star, f2_min, k2 = steepest2(x0)
print("第二个函数最优解为：", x2_star)
print("该目标函数的最小值为：", f2_min)
print("第二个函数第几次结束：", k2)