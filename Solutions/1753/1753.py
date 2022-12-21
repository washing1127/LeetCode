# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/21 10:03
# File: 1753.py
# Desc: 


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a,b,c = sorted([a,b,c])
        if c > a+b: return a+b
        return sum([a,b,c]) // 2
