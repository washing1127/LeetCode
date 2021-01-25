# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/25 17:38
# File: 0168.py
# Desc: 
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n:
            r = n % 26
            n = n // 26
            if r == 0: 
                r = 26
                n -= 1
            r += 64
            s += chr(r)
        return s[::-1]