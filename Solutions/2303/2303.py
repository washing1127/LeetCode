# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/01/23 20:21
# File: 2303.py
# Desc: 



class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ret = 0
        for idx,(a,b) in enumerate(brackets):
            if idx == 0:
                mn = min(income, a)
            else:
                mn = min(income, a) - brackets[idx-1][0]
            ret += mn * b / 100
            if income <= a: return ret
