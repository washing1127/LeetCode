# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/26 10:28
# File: 0682.py
# Desc: 

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        l = []
        for i in ops:
            if i.isdigit() or i[0]=="-" and i[1:].isdigit(): l.append(int(i))
            elif i == "+": l.append(sum(l[-2:]))
            elif i == "C": l.pop()
            elif i == "D": l.append(l[-1]*2)
        # print(l)
        return sum(l)
