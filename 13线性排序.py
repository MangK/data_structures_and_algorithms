'''
数据结构与算法之美代码实现：线性排序
'''
list = [1, 5, 3, 4, 2, 2, 7, 11, 3, 29, 12, 111, 1, 113, 2, 66, 3]
from quickSort import quickSort as q

# 桶排序
# def bucketSort():
q(list,0,len(list))
print(list)