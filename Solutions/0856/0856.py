# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/09 15:18
# File: 0856.py
# Desc: 


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        l = []
        for i in s:
            if i == "(": l.append(i)
            else:
                if l[-1] == '(': l[-1] = 1
                else:
                    idx = len(l) - 1
                    while idx >= 0:
                        if l[idx] == '(': break
                        idx -= 1
                    new = sum(l[idx+1:]) * 2
                    l = l[:idx]
                    l.append(new)
        return sum(l)
