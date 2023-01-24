# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/24 10:35
# File: 1828.py
# Desc: 


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret = []
        for x1,y1,r1 in queries:
            num = 0
            for x2, y2 in points:
                r2 = sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
                if r2 <= r1: num += 1
            ret.append(num)
        return ret

