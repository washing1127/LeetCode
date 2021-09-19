# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/19 10:49
# File: 0650.py
# Desc: 

class Solution:
    def minSteps(self, n: int) -> int:
        def f(n):
            for i in range(2,n+1):
                ys = n % i
                if ys == 0:
                    return i, n // i

        ret = 0
        while n > 1:
            cs, s = f(n)
            ret += cs
            n = s
        return ret
