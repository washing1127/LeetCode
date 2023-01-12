# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/12 10:50
# File: 1807.py
# Desc: 


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        ans, start = [], -1
        print(d)
        for i, c in enumerate(s):
            if c == '(':
                start = i
            elif c == ')':
                ans.append(d.get(s[start + 1: i], '?'))
                start = -1
            elif start < 0:
                ans.append(c)
        return "".join(ans)

