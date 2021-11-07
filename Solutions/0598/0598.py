# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/7 10:40
# File: 0598.py
# Desc: 

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mm = m
        nn = n
        for a, b in ops:
            if a < mm:
                mm = a
            if b < nn:
                nn = b
        return mm*nn
