# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/4 10:47
# File: 1796.py
# Desc: 


class Solution:
    def secondHighest(self, s: str) -> int:
        se = set()
        for i in s:
            if i.isdigit(): se.add(int(i))
        if len(se) < 2: return -1
        li = sorted(se)
        return li[-2]
