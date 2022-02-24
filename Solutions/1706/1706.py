# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/24 10:12
# File: 1706.py
# Desc: 
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        l = [[i] for i in range(n)]
        for line in grid:
            new_l = [[] for _ in line]
            for idx in range(n):
                if idx == 0 and line[idx] == -1 or idx == n-1 and line[idx] == 1: continue
                elif line[idx] == -1 and line[idx-1] == 1 or line[idx] == 1 and line[idx+1] == -1: continue
                elif line[idx] == -1: new_l[idx-1].extend(l[idx])
                elif line[idx] == 1: new_l[idx+1].extend(l[idx])
            l = new_l
        ret = [-1 for i in range(n)]
        for idx,li in enumerate(l):
            for j in li:
                ret[j] = idx
        return ret
        
