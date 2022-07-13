# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/13 10:15
# File: 0735.py
# Desc: 


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        d = []
        x = []
        for idx, i in enumerate(asteroids):
            if i > 0: d.append(idx)
            else: x.append(idx)
        ok = []
        # print(d)
        # print(x)
        for xidx0 in x:
            if not d or xidx0 < d[0]: # 没有正数或当前负数最靠左
                ok.append(xidx0)
                continue
            for l2 in range(len(d)):
                if d[l2] > xidx0:
                    l2 -= 1
                    break
            f = False
            l = 0
            r = len(d) - 1
            while l<r:
                m = (l+r)//2
                if d[m] > xidx0: r=m
                else:
                    f = True
                    l = m+1
            if f and d[r] > xidx0: l-=1
            # print(xidx0,d,l2,l)
            # print(xidx0,l)
            while l >= 0:
                if asteroids[d[l]] > asteroids[xidx0] * -1:
                    break
                elif asteroids[d[l]] == asteroids[xidx0] * -1:
                    d.pop(l)
                    break
                else:
                    d.pop(l)
                    l -= 1
            if l == -1: ok.append(xidx0)
        ok += d
        ok.sort()
        ret = [asteroids[i] for i in ok]
        return ret
