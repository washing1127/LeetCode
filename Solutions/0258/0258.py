# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/03 10:52
# File: 0258.py
# Desc: 

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            n = num % 10
            while num:
                num //= 10
                n += num % 10
            num = n
        return num
