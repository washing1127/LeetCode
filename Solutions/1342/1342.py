# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/31 12:06
# File: 1342.py
# Desc: 

class Solution:
    def numberOfSteps(self, num: int) -> int:
        ret = 0
        while num > 0:
            if num % 2: num -= 1
            else: num //= 2
            ret += 1
        return ret
