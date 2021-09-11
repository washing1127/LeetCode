# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/30 11:12
# File: 0074.py
# Desc: 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        li = [i[0] for i in matrix]
        if matrix[0][0] > target: return False
        for idx, num in enumerate(li):
            if num > target: break
        else:
            idx += 1
        idx -= 1

        li = matrix[idx] 
        for i, num in enumerate(li):
            if num >= target: break
        return li[i] == target