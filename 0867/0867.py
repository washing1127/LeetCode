# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/5 18:11
# File: 0830.py
# Desc: 

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # m = len(matrix)
        # n = len(matrix[0])
        # ret = []
        # for i in range(n):
        #     l = []
        #     for j in range(m):
        #         l.append(matrix[j][i])
        #     ret.append(l)

        # return ret

        return list(zip(*matrix))