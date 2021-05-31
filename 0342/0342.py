# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/31 9:59
# File: 0342.py
# Desc: 

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        c = collections.Counter(bin(n)[3:])
        return n >= 1 and c['1'] == 0 and c['0'] % 2 == 0