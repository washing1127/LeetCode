# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/1 17:52
# File: 1694.py
# Desc: 


class Solution:
    def reformatNumber(self, number: str) -> str:
        l = []
        for i in number:
            if i in ' -': continue
            if not l or len(l[-1]) == 3: l.append(i)
            else: l[-1] += i
        if len(l[-1]) == 1:
            l[-1] = l[-2][-1] + l[-1]
            l[-2] = l[-2][:-1]
        return '-'.join(l)
