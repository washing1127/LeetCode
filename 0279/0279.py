# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/11 11:20
# File: 0279.py
# Desc: 

class Solution:
    def numSquares(self, n: int) -> int:
        pfs = set()
        for i in range(1, 101): pfs.add(i**2)

        def ck4(num):
            while num % 4 == 0: num //= 4
            return num %  8 == 7

        if n in pfs: return 1
        if ck4(n): return 4
        for i in range(1, int(math.sqrt(n))+1):
            j = n - i ** 2
            if j in pfs: return 2
        return 3
