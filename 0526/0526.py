# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/16 11:01
# File: 0526.py
# Desc: 

class Solution:
    def countArrangement(self, n: int) -> int:
        # l = [1,2,3,8,10,36,41,132,250,700,750,4010,4237,10680,24679]
        # return l[n-1]class Solution:

        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]
        
        return f[(1 << n) - 1]

