# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/15 11:30
# File: 1380.py
# Desc: 

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        l1 = [[False]*n for i in range(m)]
        l2 = [[False]*n for i in range(m)]
        for idx, lm in enumerate(matrix):
            mi = min(lm)
            for jdx, num in enumerate(lm):
                if num == mi: l1[idx][jdx] = True
        for jdx in range(n):
            ln = [l[jdx] for l in matrix]
            ma = max(ln)
            for idx,num in enumerate(ln):
                if num == ma: l2[idx][jdx] = True
        ret = []
        for idx, lm in enumerate(matrix):
            for jdx, num in enumerate(lm):
                if l1[idx][jdx] and l2[idx][jdx]: ret.append(num)
        return ret
