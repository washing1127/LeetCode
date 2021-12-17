# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/17 15:33
# File: 1518.py
# Desc: 

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles
        while numBottles > 0:
            ys = numBottles % numExchange if numBottles > numExchange else 0
            s = numBottles // numExchange
            ret += s
            numBottles = s+ys
        return ret
