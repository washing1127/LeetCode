# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/20 20:28
# File: 1260.py
# Desc: 

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid); n = len(grid[0])
        l = [i for j in grid for i in j]
        k %= len(l)
        ret = [[0]*n for _ in range(m)]
        idx = len(l) - k
        for i in range(m):
            for j in range(n):
                if idx == len(l): idx=0
                ret[i][j] = l[idx]
                idx+=1
        return ret
