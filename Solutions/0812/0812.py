# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/15 10:18
# File: 0812.py
# Desc: 


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2
        return max(triangleArea(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))
                ret = min(ret, dis[site])
        return -1 if ret == inf else ret


