# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/25 10:10
# File: 1688.py
# Desc: 

class Solution:
    def numberOfMatches(self, n: int) -> int:
        ret = 0
        while n > 1:
            ys = n % 2
            n //= 2
            ret += n
            n += ys
        return ret
