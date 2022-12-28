# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/28 10:03
# File: 1750.py
# Desc: 

class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s) >= 2 and s[0] == s[-1]:
            s = s.strip(s[0])
        return len(s)
