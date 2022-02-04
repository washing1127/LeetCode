# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/4 12:41
# File: 1725.py
# Desc: 
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l = [min(i) for i in rectangles]
        c = collections.Counter(l)
        m = max(c.keys())
        return c[m]
