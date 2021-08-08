# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/8 11:05
# File: 1137.py
# Desc: 


class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1, 2]
        if n <= 3: return l[n]
        for i in range(n-4):
            s = sum(l[-3:])
            l.append(s)
        return sum(l[-3:])