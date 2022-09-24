# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/24 10:40
# File: 1652.py
# Desc: 


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0: return [0] * n
        l = []
        for i in range(n):
            if k < 0:
                s = i + k
                e = i
                if s >= 0 or e < 0: l.append(sum(code[s:e]))
                else: l.append(sum(code[s:]) + sum(code[:e]))
            else:
                s = i + 1
                e = s + k
                if e < n: l.append(sum(code[s:e]))
                elif s <= n: l.append(sum(code[s:]) + sum(code[:e%n]))
                else: l.append(sum(code[s%n:e%n]))
        return l
