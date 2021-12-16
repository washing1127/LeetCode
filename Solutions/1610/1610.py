# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/16 11:15
# File: 1610.py
# Desc: 

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        sameCnt = 0
        polarDegrees = []
        for p in points:
            if p == location:
                sameCnt += 1
            else:
                polarDegrees.append(atan2(p[1] - location[1], p[0] - location[0]))
        polarDegrees.sort()

        n = len(polarDegrees)
        polarDegrees += [deg + 2 * pi for deg in polarDegrees]

        maxCnt = 0
        right = 0
        degree = angle * pi / 180
        for i in range(n):
            while right < n * 2 and polarDegrees[right] <= polarDegrees[i] + degree:
                right += 1
            maxCnt = max(maxCnt, right - i)
        return sameCnt + maxCnt

