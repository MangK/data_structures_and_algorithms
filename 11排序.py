'''
数据结构与算法之美代码实现：排序
---
原地排序：原地排序算法，就是特指空间复杂度是 O(1) 的排序算法。
稳定排序：如果要排序的两个值相等，则不会交换位置
'''
list = [1, 5, 3, 4, 2, 2, 7, 11, 3, 29, 12]


# 冒泡排序(原地排序；稳定排序)
def bubbleSort(list):
    count = len(list)
    for i in range(count):
        flag = False
        for j in range(0, count - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                flag = True
        if not flag: break


# 插入排序(原地排序；稳定排序)
def insertionSort(list):
    i = 1
    count = len(list)
    while i < count:
        val = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > val:
                list[j + 1] = list[j]
            else:
                break
            j -= 1
        i += 1
        list[j + 1] = val


# 选择排序(原地排序；非稳定排序)
def selectionSort(list):
    count = len(list)
    for i in range(count):
        min = list[i]
        flag = i
        j = i + 1
        while j < count:
            if list[j] < min:
                min = list[j]
                flag = j
            j += 1
        list[i], list[flag] = list[flag], list[i]



# # (自己的)插入排序
# def insertionSort2(list):
#     count = len(list)
#     # id1 = id(list)
#     for i in range(count):
#         list, val = list[0:count - 1], list[count - 1: count]  # 注意list还是不是原来的list（id是否已经发生了改变）
#         # id2 = id(list)
#         for j in range(1, count):
#             if val[0] < list[j - 1]:
#                 leftList, rightList = list[0: j - 1], list[j - 1: count]
#                 list = leftList + val + rightList
#                 break
#             if j == count - 1:
#                 list = list + val  # 注意list还是不是原来的list（id是否已经发生了改变）
#                 # id3 = id(list)
#     # id4 = id(list)
#     return list
