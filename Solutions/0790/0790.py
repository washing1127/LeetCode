# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/128 8:48
# File: 0790.py
# Desc: 


class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        a,b,c=1,2,5
        for i in range(3,n):
            d=c*2+a
            a,b,c = b,c,d
        return c%(10**9+7)