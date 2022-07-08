# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/8 10:52
# File: 1217.py
# Desc: 


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        c = collections.Counter(position)
        j = 0
        o = 0
        for idx,i in c.items():
            if idx % 2 == 0: o += i
            else: j += i
        return min(j, o)
