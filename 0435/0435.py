# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/31 10:14
# File: 0435.py
# Desc: 

class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        count = 0
        for i in intervals[1:]:
            if i[0] >= end:
                end = i[1]
                continue
            if i[1] < end:
                end = i[1]
            count += 1

        return count
