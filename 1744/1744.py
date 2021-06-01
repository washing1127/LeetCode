# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/1 13:57
# File: 1744.py
# Desc: 
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        num = 1
        li = []
        for i in candiesCount:
            li.append([num, num+i-1])
            num = num + i
        ret = []
        for i in range(len(queries)):
            a, b, c = queries[i]
            b = b+1
            if li[a][0] <= b <= li[a][1]: ret.append(True)
            elif li[a][0] > b and li[a][0] <= b * c: ret.append(True)
            else: ret.append(False)

        return ret
