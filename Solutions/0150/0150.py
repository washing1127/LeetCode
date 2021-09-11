# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/20 16:21
# File: 0150.py
# Desc: 


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = tokens[:2]
        for i in tokens[2:]:
            if i in "+-*/":
                r = stk.pop()
                l = stk.pop()
                num = int(eval(l+i+r))
                stk.append(str(num))
            else:
                stk.append(i)
        return eval(stk[0])