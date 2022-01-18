# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/18 10:2222
# File: 0539.py
# Desc: 

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def p(s):
            h,m = s.split(":")
            return int(h)*60+int(m)
        tp = [p(i) for i in timePoints]
        tp.sort()
        ret = 24*60
        tp.append(tp[0]+ret)
        for i in range(len(tp)-1,0, -1):
            r = tp[i]
            l = tp[i-1]
            ret = min(ret, r-l)
        return ret
