# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/10 9:15
# File: 0441.py
# Desc: 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # (a+b)*b/2=n
        # n*2/(b*(b+1))
        # b+1 > math.sqrt(n*2) > b
        b = int(math.sqrt(n*2))
        if b*(b+1)/2 <= n: return b
        else: return b - 1
