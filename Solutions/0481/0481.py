# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/31 07:56
# File: 0481.py
# Desc: 


class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3: return 1
        l = [1,2,2]
        gai = 1
        idx = 2
        for _ in range(2, n):
            l.extend([gai] * l[idx])
            idx += 1
            if gai == 1: gai = 2
            else: gai = 1
            if len(l) >= n:
                return sum([i%2 for i in l[:n]])
