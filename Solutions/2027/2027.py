# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/27 10:16
# File: 2027.py
# Desc: 


class Solution:
    def minimumMoves(self, s: str) -> int:
        ret = 0
        l = list(s)
        for i in range(len(l)):
            if l[i] == "X":
                l[i:i+3] = ['O','O','O']
                ret += 1
        return ret
