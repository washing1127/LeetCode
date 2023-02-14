# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/14 11:05
# File: 1124.py
# Desc: 


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n+1)
        stk = [0]
        for i in range(1,n+1):
            s[i] = s[i-1] + (1 if hours[i-1] > 8 else -1)
            if s[stk[-1]] > s[i]:
                stk.append(i)
        res = 0
        for r in range(n,0,-1):
            while stk and s[stk[-1]] < s[r]:
                res = max(res, r-stk.pop())
        return res
