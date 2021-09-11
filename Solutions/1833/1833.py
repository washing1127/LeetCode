# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/2 10:35
# File: 1833.py
# Desc: 
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = 0
        for i in costs:
            if coins < i: break
            n += 1
            coins -= i
        return n
