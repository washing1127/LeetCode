# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/5 11:33
# File: 0521.py
# Desc: 

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b: return -1
        else: return len(a) if len(a) > len(b) else len(b)
