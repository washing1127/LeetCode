# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/31 10:21
# File: 2319.py
# Desc: 


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            if grid[i][i] == 0 or grid[i][n-1-i] == 0:
                return False
            if i == n-1-i:
                if grid[i][i] != sum(grid[i]):
                    return False
            elif grid[i][i]+grid[i][n-1-i] != sum(grid[i]):
                return False
        return True
