# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/1 10:21
# File: 2022.py
# Desc: 

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ret = []
        idx = 0
        if len(original) != m*n: return ret
        for i in range(m):
            ret.append([])
            for j in range(n):
                ret[-1].append(original[idx])
                idx+=1
        return ret
