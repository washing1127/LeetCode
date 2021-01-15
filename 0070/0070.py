# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/15 10:33
# File: 0070.py
# Desc: 
class Solution:
    def climbStairs(self, n: int) -> int:
        num = 1
        sumNum = 2
        if n == 1: return num
        if n == 2: return sumNum
        for i in range(n-2):
            sumNum, num = num+sumNum, sumNum
        return sumNum