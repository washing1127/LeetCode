# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/30 16:08
# File: 0231.py
# Desc: 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        elif n == 1: return True
        else: return bin(n).count("1") == 1