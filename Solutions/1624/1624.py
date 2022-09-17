# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/17 22:14
# File: 1624.py
# Desc: 

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ma = -1
        for idx in range(len(s)):
            ma = max(s.rfind(s[idx]) - idx, ma)
        return ma-1
