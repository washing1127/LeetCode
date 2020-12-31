# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/31 11:40
# File: 0006.py
# Desc: 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 2 or numRows <= 1: return s
        step = 1
        idx = 0
        dic = {}
        ret = ''
        for i in range(numRows):
            dic[i] = ''
        for i in s:
            dic[idx] += i
            idx += step

            if idx == 0 or idx == numRows - 1:
                step *= -1
        for i in range(numRows):
            ret += dic[i]

        return ret
