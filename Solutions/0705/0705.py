# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/13 23:31
# File: 0705.py
# Desc: 

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = list()


    def add(self, key: int) -> None:
        if not key in self.s:
            self.s.append(key)


    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.s



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)