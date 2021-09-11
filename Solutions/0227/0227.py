# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/11 16:17
# File: 0227.py
# Desc: 

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '').replace("+", " + ").replace("-", " - ").replace('/', '//')
        l = s.split(' ')
        for i in range(len(l)):
            if l[i] != '+' and l[i] != '-':
                l[i] = str(eval(l[i]))
        return eval(''.join(l))