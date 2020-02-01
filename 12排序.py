'''
数据结构与算法之美代码实现：排序
---
原地排序：原地排序算法，就是特指空间复杂度是 O(1) 的排序算法。
稳定排序：如果要排序的两个值相等，则不会交换位置
'''
list = [1, 5, 3, 4, 2, 2, 7, 11, 3, 29, 12, 111, 1, 113, 2, 66, 3]


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


# 快速排序(原地排序;不稳定排序)
def quickSort(list, l, r):
    if l < r:
        q = partition(list, l, r)
        quickSort(list, l, q - 1)
        quickSort(list, q + 1, r)


def partition(list, l, r):
    x = list[r]
    i = l - 1
    for j in range(l, r):
        if list[j] <= x:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[r] = list[r], list[i + 1]
    return i + 1


# 这里也是快速排序的实现，但是因为频繁的申请内存，性能与效率不如上面一种
def quickSort1(list):
    if len(list) <= 1: return list
    flag = list[len(list) - 1:]
    left = []
    right = []
    for i in range(len(list) - 1):
        if flag[0] > list[i]:
            left.append(list[i])
        else:
            right.append(list[i])
    return quickSort1(left) + flag + quickSort1(right)

print(quickSort1(list))