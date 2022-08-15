# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/15 10:40
# File: 0641.py
# Desc: 


class MyCircularDeque:

    def __init__(self, k: int):
        self.l = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.l) < self.k:
            self.l.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.l) < self.k:
            self.l.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.l:
            self.l.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if self.l:
            self.l.pop()
            return True
        return False

    def getFront(self) -> int:
        if self.l:
            return self.l[0]
        return -1

    def getRear(self) -> int:
        if self.l:
            return self.l[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.l) == 0

    def isFull(self) -> bool:
        return len(self.l) == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()

