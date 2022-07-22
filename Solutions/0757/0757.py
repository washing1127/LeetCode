# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/22 10:18
# File: 0757.py
# Desc: 


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0], reverse=True)
        temp = [intervals[0][0], intervals[0][0]+1]
        ret = 2
        for s,e in intervals[1:]:
            if temp[0] > e:
                temp[0] = s
                temp[1] = s+1
                ret += 2
            elif temp[1] > e:
                temp[1] = temp[0]
                temp[0] = s
                ret += 1
        return ret
