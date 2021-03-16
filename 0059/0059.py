# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/16 14:16
# File: 0059.py
# Desc: 
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1: return [[1]]
        ret = []
        for i in range(n): ret.append([0]*n)
        l = 0
        u = 1
        r = d = n - 1
        step = 1
        case = 1

        row = 0
        col = 0

        num = 1
        
        while l <= r or u <= d:
            ret[row][col] = num
            if case == 1:
                col += step
                if col == r:
                    r -= step
                    case = 2
            elif case == 2:
                row += step
                if row == d:
                    d -= step
                    case = 3
                    step *= -1
            elif case == 3:
                col += step
                if col == l:
                    l -= step
                    case = 4
            elif case == 4:
                row += step
                if row == u:
                    u -= step
                    case = 1
                    step *= -1
            num += 1
        ret[row][col] = num
        return ret