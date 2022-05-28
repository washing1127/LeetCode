# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/28 10:09
# File: 1021.py
# Desc: 

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, stack = "", []
        for c in s:
            if c == ')':
                stack.pop()
            if stack:
                res += c
            if c == '(':
                stack.append(c)
        return res

