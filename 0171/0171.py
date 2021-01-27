# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/27 10:34
# File: 0171.py
# Desc: 

class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for i in s:
            n = n * 26 + ord(i) - 64
        return n