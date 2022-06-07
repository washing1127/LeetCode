# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/7 16:04
# File: 0875.py
# Desc: 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return bisect_left(range(max(piles)), -h, 1, key=lambda k: -sum((pile + k - 1) // k for pile in piles))

