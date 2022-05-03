# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/3 10:35
# File: 1823.py
# Desc: 


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1,n+1))
        idx = 0
        ct = 0
        while n > 1:
            num = l[idx]
            ct += 1
            if ct == k:
                ct = 0
                l.remove(num)
                n -= 1
            else:idx += 1
            if idx >= len(l): idx = 0
        return l[0]
