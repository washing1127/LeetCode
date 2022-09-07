# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/7 10:33
# File: 1592.py
# Desc: 


class Solution:
    def reorderSpaces(self, text: str) -> str:
        ns = text.count(" ")
        l = [i for i in text.split(" ") if i]
        if len(l) == 1: return l[0] + ' '*ns
        n1 = ns // (len(l)-1)
        n2 = ns % (len(l)-1)
        return (" "*n1).join(l) + " "*n2
