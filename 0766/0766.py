# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/22 22:48
# File: 0766.py
# Desc: 

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for line in range(n-1):
            m_list = matrix[line]
            for idx, num in enumerate(m_list[:-1]):
                if matrix[line+1][idx+1] != num:
                    return False
        return True
