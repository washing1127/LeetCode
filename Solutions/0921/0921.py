# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/4 11:01
# File: 0921.py
# Desc: 


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = []
        for i in s:
            if i == ')':
                if l and l[-1] == '(': 
                    l.pop()
                    continue
            l.append(i)
        return len(l)
