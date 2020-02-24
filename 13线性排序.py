'''
数据结构与算法之美代码实现：线性排序
'''
import math

list = [1, 5, 3, 4, 2, 2, 7, 11, 3, 29, 12, 116, 1, 113, 2, 66, 3]
from quickSort import quickSort as quick


# 桶排序的实现
# flag:桶的数量
# item: 桶的范围区间大小
# bucket:定义的桶
def bucketSort(list, min=min(list), max=max(list), flag=5):
    item = math.ceil((max - min) / flag)
    bucket = [[] for n in range(flag)]
    for i in range(len(list)):
        for j in range(flag):
            if min + item * j <= list[i] < min + item * (j + 1):
                bucket[j] += [list[i]]
    res = []
    for x in bucket:
        quick(x, 0, len(x) - 1)
        res += x
    return res


x = bucketSort(list)
print(x)
