# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/15 11:30
# File: OfferII041.py
# Desc: 


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.sz = size
        self.sm = 0

    def next(self, val: int) -> float:
        self.l.append(val)
        self.sm += val
        if len(self.l) > self.sz:
            num = self.l.pop(0)
            self.sm -= num
        return self.sm / len(self.l)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
