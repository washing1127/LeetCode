# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/26 10:20
# File: 0371.py
# Desc: 

MASK1 = 4294967296  # 2^32
MASK2 = 2147483648  # 2^31
MASK3 = 2147483647  # 2^31-1

class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = ((a & b) << 1) % MASK1
            a = (a ^ b) % MASK1
            b = carry
        if a & MASK2:  # 负数
            return ~((a ^ MASK2) ^ MASK3)
        else:  # 正数
            return a

