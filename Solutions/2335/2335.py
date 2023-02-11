# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/11 20:21
# File: 2331.py
# Desc: 


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a,b,c = sorted(amount)
        dy = b - a
        c1 = c - dy
        c2 = c1 // 2
        c3 = c1 - c2
        a -= c2
        # b
        return c + max(a,0)
