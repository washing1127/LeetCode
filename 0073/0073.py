# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/21 14:19
# File: 0073.py
# Desc: 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        lm = [False] * m 
        ln = [False] * n
        for i in range(m):
            row = matrix[i]
            for j in range(n):
                col = row[j]
                if col == 0:
                    ln[j] = True
                    lm[i] = True
        for i in range(m):
            if lm[i]:
                matrix[i] = [0] * n
            else:
                for j in range(n):
                    if ln[j]:
                        matrix[i][j] = 0
