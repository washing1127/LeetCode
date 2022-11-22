# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/23 7:32
# File: 1742.py
# Desc: 

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = dict()
        for i in range(lowLimit, highLimit+1):
            t = 0
            n = i
            while n:
                t += n % 10
                n //= 10
            if t in d: d[t] += 1
            else: d[t] = 1
        return max(d.values())
