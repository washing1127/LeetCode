# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/11 11:13
# File: 1417.py
# Desc: 


class Solution:
    def reformat(self, s: str) -> str:
        s1 = []
        s2 = []
        for i in s:
            if i.isalpha(): s1.append(i)
            else: s2.append(i)
        if abs(len(s1) - len(s2)) > 1: return ''
        if len(s1) > len(s2): s1, s2 = s2, s1
        ret = ''
        for i,j in zip(s1,s2):
            ret += j + i
        if len(s2) > len(s1): ret += s2[-1]
        return ret
