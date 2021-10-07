# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/7 10:14
# File: 0434.py
# Desc: 

class Solution:
    def countSegments(self, s: str) -> int:
        if not s.strip(): return 0
        while "  " in s: s = s.replace("  ", " ")
        return s.strip().count(" ")+1


