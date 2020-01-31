'''
数据结构与算法之美代码实现：因为引入哨兵导致的代码执行效率差别
'''
arr = [4, 2, 3, 5, 9, 6]
n = len(arr)
key = 6

'''
在 arr 很大的情况下，因为我们省略掉了 i < n ，find2() 的执行效率会比 find1()
'''


def find1(a, n, key):
    if (len(a) == 0 or n <= 0):
        return -1
    i = 0
    while (i < n):
        if (a[i] == key):
            return i
        i += 1
    return -1


def find2(a, n, key):
    if (len(a) == 0 or n <= 0):
        return -1
    if (a[n - 1] == key):
        return n - 1
    tmp = a[n - 1]
    a[n - 1] = key
    i = 0
    while a[i] != key:
        i += 1
    a[n - 1] = tmp
    if (i == n - 1):
        return -1
    return i