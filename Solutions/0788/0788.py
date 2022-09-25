# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/25 12:03
# File: 0788.py
# Desc: 


class Solution:
    def rotatedDigits(self, n: int) -> int:
        ret = 0
        # l = []
        for i in range(n+1):
            s = str(i)
            for j in '347':
                if j in s: break
            else:
                for j in '2569':
                    if j in s: break
                else: continue
                ret += 1
                # l.append(i)
        # print(l)
        return ret
