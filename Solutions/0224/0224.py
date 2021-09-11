# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/10 11:48
# File: 0224.py
# Desc: 

class Solution:
    def calculate(self, s: str) -> int:

        ans = 0
        stk = ''
        for i in s:
            if i == ' ': continue
            elif i == ')':
                l, r = stk.rsplit('(', 1)
                stk = l + str(eval(r))
            else:
                stk += i
        return eval(stk)