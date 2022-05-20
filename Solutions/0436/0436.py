# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/20 10:14
# File: 0436.py
# Desc: 

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s2id = dict()
        sl = list()
        for idx, (s,e) in enumerate(intervals):
            s2id[s] = idx
            sl.append(s)
        sl.sort()
        ret = list()
        for s, e in intervals:
            l=0
            r=len(sl)-1
            if sl[r] < e:
                ret.append(-1)
                continue
            while l < r:
                m = (l+r)//2
                if sl[m] >= e: r = m
                else: l = m+1
            ret.append(s2id[sl[l]])
        return ret
