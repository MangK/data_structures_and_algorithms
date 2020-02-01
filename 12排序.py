'''
数据结构与算法之美代码实现：排序
---
原地排序：原地排序算法，就是特指空间复杂度是 O(1) 的排序算法。
稳定排序：如果要排序的两个值相等，则不会交换位置
'''
list = [1, 5, 3, 4, 2, 2, 7, 11, 3, 29, 12]


# 归并排序(时间复杂度为O(nlogn):稳定排序)
def mergeSort(list):
    if len(list) <= 1: return list
    mid = len(list) // 2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])
    return merge(left, right)


def merge(left, right):
    list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1
    list += left[i:]
    list += right[j:]
    return list
