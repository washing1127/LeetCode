# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/27 10:40
# File: 0592.py
# Desc: 


class Solution:
    def fractionAddition(self, expression: str) -> str:
        l = expression.replace("+", " ").replace("-", " -").strip().split(" ")
        l = [map(eval, i.split("/")) for i in l]
        fz1 = 0
        fm1 = 1
        for fz2,fm2 in l:
            fz1 = fz1*fm2 + fz2*fm1
            fm1 *= fm2
        if fz1 == 0: return '0/1'
        if fz1 % fm1 == 0: return f'{fz1//fm1}/1'
        a, b = fz1,fm1
        while fm1 > 0:
            fz1, fm1 = fm1, fz1%fm1
        return f'{a//fz1}/{b//fz1}'
