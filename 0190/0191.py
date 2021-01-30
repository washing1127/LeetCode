# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/30 11:52
# File: 0190.py
# Desc: 
class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        s = bin(n)[2:]
        s = "0"*(32-len(s))+s
        for idx, i in enumerate(s):
            num += 2**idx*int(i)
        return num