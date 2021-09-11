# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/13 14:18
# File: 0233.py
# Desc: 

class Solution:
    def countDigitOne(self, n: int) -> int:
        ret = 0
        i = 0
        while n >= 10**i:
            ret += n // 10**(i+1) * 10**i + min(max(n % 10**(i+1) - 10**i + 1, 0), 10**i)
            i += 1
        return ret
