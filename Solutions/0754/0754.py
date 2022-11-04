# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/4 10:18
# File: 0754.py
# Desc: 


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        total = 0
        i = 0
        while total < target or (total - target) % 2 != 0:
            i += 1
            total += i
        return i
