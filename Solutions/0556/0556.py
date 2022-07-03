# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/3 11:30
# File: 0556.py
# Desc: 



class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        l = list(s)
        passed = []
        for i in range(len(s)-1,-1,-1):
            for p in passed:
                if p > s[i]:
                    np = passed.copy()
                    np.remove(p)
                    np.append(s[i])
                    l[i] = p
                    res = int(str(''.join(l[:i+1]+sorted(np))))
                    if res < 2**31: return res
            passed.append(s[i])
            passed.sort()
        return -1
