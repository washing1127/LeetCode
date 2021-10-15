# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/30 19:05
# File: 0038.py
# Desc: 

class Solution:
    def countAndSay(self, n: int) -> str:
        def desc(s0):
            s1 = ''
            c = s0[0]
            num = 1
            for i in s0[1:]:
                if c == i:
                    num += 1
                else:
                    s1 += str(num)+c
                    num = 1
                    c = i
            s1 += str(num)+c
            return s1
        s = '1'
        for i in range(1,n):
            s = desc(s)
        return s
