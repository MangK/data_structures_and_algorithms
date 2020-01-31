class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LianBiao(object):
    def __init__(self):
        self.root = None

    def addNode(self, data):
        if self.root == None:
            self.root = Node(data=data, next=None)
            return self.root
        else:
            # 有头结点，则需要遍历到尾部节点，进行链表增加操作
            cursor = self.root
            while cursor.next != None:
                cursor = cursor.next
            cursor.next = Node(data=data, next=None)
            return self.root
