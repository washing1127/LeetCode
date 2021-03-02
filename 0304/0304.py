# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/2 8:41
# File: 0304.py
# Desc: 

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for line in self.matrix[row1: row2+1]:
            for item in line[col1: col2+1]:
                ans += item
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)