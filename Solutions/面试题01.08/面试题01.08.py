# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/30 8:36
# File: 面试题 01.08.py
# Desc: 


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        s1 = set()
        s2 = set()
        for i, l in enumerate(matrix):
            for j, n in enumerate(l):
                if n == 0:
                    s1.add(i)
                    s2.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in s1 or j in s2: matrix[i][j] = 0
