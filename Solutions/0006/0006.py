# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/31 11:40
# File: 0006.py
# Desc: 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        l = [''] * numRows
        idx = 0
        fx = -1
        for i in s:
            l[idx] += i
            if idx == 0 or idx == numRows-1: fx *= -1
            idx += fx
        return ''.join(l)
