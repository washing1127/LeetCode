# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/06/08 10:13
# File: 1037.py
# Desc: 

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1,y1),(x2,y2),(x3,y3) = points
        return (y3-y1)*(x2-x1) != (y2-y1)*(x3-x1)
