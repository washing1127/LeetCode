# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/ 10:17
# File: 1779.py
# Desc: 


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ret = -1
        oldjl = 10000
        for idx, (a,b) in enumerate(points):
            if a == x or b == y:
                jl = abs(a-x) + (abs(b-y))
                if jl < oldjl:
                    oldjl = jl
                    ret = idx
        return ret
