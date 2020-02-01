'''
数据结构与算法之美代码实现：队列的实现
'''


# 顺序队列
class List():
    def __init__(self, canAdd=False):
        self.basicList = [None, None, None, None, None]
        self.list = self.basicList[:]
        self.maxLen = len(self.basicList)
        self.head = 0
        self.tail = 0
        self.canAdd = canAdd
        self.count = 0

    # 允许自增扩容列表
    def _add(self):
        self.list += self.basicList
        self.maxLen += len(self.basicList)

    # 不允许自增移动元素，超出长度报错
    def _reBuild(self):
        if self.count == self.maxLen:
            return False
        tmp = self.list[self.head:self.maxLen] + self.basicList  # 列表先切片后拓展
        self.list = tmp[0:self.maxLen]  # 切片到指定长度
        self.head = 0  # 重置头部指针
        self.tail = self.count  # 重置尾部指针
        return True

    # 队列新增元素
    def enQueue(self, data):
        if self.tail == self.maxLen:
            if self.canAdd:
                self._add()
            else:
                if self.head == self.tail:  # 如果首尾指针都指向了最后，说明队列没有元素了，直接重置指针即可
                    self.head = self.tail = 0
                if not self._reBuild():
                    return '队列已满'
        self.list[self.tail] = data
        self.tail += 1
        self.count += 1
        return True

    # 队列弹出元素
    def deQueue(self):
        if self.count == 0:
            return '队列已空'
        tmp = self.list[self.head]
        self.list[self.head] = None
        self.head += 1
        self.count -= 1
        return tmp

# 环形队列
