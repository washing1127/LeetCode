# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/23 15:38
# File: 0707.py
# Desc: 


class MyLinkedList:

    def __init__(self):
        self.l = list()

    def get(self, index: int) -> int:
        if index < len(self.l):
            return self.l[index]
        else: return -1

    def addAtHead(self, val: int) -> None:
        self.l.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.l.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
        elif index > len(self.l):
            pass
        else:
            self.l.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.l):
            self.l.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
