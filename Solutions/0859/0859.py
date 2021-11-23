# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/23 15:18
# File: 0859.py
# Desc: 

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if not len(goal) == n: return False
        if s == goal:
            if n == len(set(s)): return False
            else: return True
        else:
            l = []
            for i in range(n):
                c1 = s[i]
                c2 = goal[i]
                if not c1 == c2: l.append(i)
            if not len(l) == 2: return False
            a,b = l
            if s[a] != goal[b] or s[b] != goal[a]: return False
            return True
