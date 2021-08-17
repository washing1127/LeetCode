# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/17 16:00
# File: 0551.py
# Desc: 

class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for i in s:
            if i == "L": l += 1
            else:
                l = 0
                if i == "A": a += 1
            if l >= 3 or a >= 2: return False
        return True