# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/15 15:13
# File: 0054.py
# Desc: 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        line = len(matrix)
        if not line: return []
        length = len(matrix[0])
        if not length: return []

        elif line == 1:
            return matrix[0]
        elif length == 1:
            return [i[0] for i in matrix]
        else:
            a = matrix[0][:-1]
            b = [i[-1] for i in matrix]
            c = matrix[-1][-2:0:-1]
            d = [i[0] for i in matrix[-1:0:-1]]
            rest = [i[1:-1] for i in matrix[1:-1]]
            return a+b+c+d+self.spiralOrder(rest)