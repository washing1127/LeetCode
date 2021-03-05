# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/5 10:12
# File: 0232.py
# Desc: 

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.l.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.l.pop(0)


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.l[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.l



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()