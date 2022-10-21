# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/21 11:16
# File: 0901.py
# Desc: 



class StockSpanner:

    def __init__(self):
        self.l = []
        self.idx = 0

    def next(self, price: int) -> int:
        while self.l:
            if price >= self.l[-1][0]:
                self.l.pop()
            else: break
        self.l.append([price, self.idx])
        self.idx+=1
        if len(self.l) == 1: return self.l[-1][1]+1
        else: return self.l[-1][1] - self.l[-2][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
