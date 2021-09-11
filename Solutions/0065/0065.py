# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/17 10:34
# File: 0065.py
# Desc: 

class Solution:
    def isNumber(self, s: str) -> bool:
        if s == 'e' or 'f' in s: return False
        try:
            float(s)
            return True
        except: return False
