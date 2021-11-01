# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/1 11:24
# File: 0575.py
# Desc: 

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set(candyType)
        n = len(candyType) // 2
        return min(len(s), n)
