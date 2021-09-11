# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/11 18:49
# File: 0264.py
# Desc: 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = {1}
        while len(s) < 5000:
            for i in s.copy():
                s.add(i * 2)
                s.add(i * 3)
                s.add(i * 5)
        l = list(s)
        l.sort()
        return l[n-1]