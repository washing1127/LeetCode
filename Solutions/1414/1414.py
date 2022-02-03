# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/3 9:30
# File: 1414.py
# Desc: 

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        l = []
        a=1
        b=1
        while a <= k:
            l.append(a)
            a,b = b,a+b
        ret = 0
        r = len(l)
        while k:
            for i in range(r-1,0,-1):
                num = l[i]
                if k >= num:
                    k -= num
                    r = i
                    ret += 1
                    break
        return ret
