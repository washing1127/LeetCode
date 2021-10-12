# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/12 17:58
# File: 0029.py
# Desc: 

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1: return 2147483647
        if dividend * divisor < 0: neg = -1
        else: neg = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        l = 0; r = dividend
        while l < r:
            m = (l + r) >> 1
            if m*divisor <= dividend and (m+1)*divisor >= dividend:
                if (m+1)*divisor == dividend: return (m+1) * neg
                else: return m * neg
            elif m*divisor > dividend: r = m
            else: l = m + 1
        return 0
        
