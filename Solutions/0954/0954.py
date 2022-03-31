# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/4/1 11:00
# File: 0954.py
# Desc: 

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def index(li,num):
            l = 0; r = len(li)
            while l < r:
                m = (l+r)//2
                if li[m] >= num: r=m
                else: l=m+1
            return l
        if arr.count(0) % 2 == 1: return False
        z = []; f = []
        for i in arr:
            if i >= 0: z.append(i)
            else: f.append(i)
        z.sort()
        f.sort()
        if len(z) % 2: return False
        cz = collections.Counter(z)
        cf = collections.Counter(f)
        while z:
            num = z[0]*2
            if cz[num]:
                cz[z[0]] -= 1
                cz[num] -= 1
                z.pop(index(z,num))
                z.pop(0)
            else: return False
        while f:
            num = f[-1]*2
            if cf[num]:
                cf[num] -= 1
                cf[f[-1]] -= 1
                f.pop(index(f,num))
                f.pop(-1)
            else: return False
        return True
