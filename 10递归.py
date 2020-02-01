'''
数据结构与算法之美代码实现：递归
'''
import sys


def fun(n):
    if n == 1:
        return n
    return fun(n - 1) + 1


print(fun(int(sys.argv[1])))
