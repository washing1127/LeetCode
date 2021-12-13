# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/13 23:12
# File: 0807.py
# Desc: 

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = list(map(max, grid))
        colMax = list(map(max, zip(*grid)))
        return sum(min(rowMax[i], colMax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))

