# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/24 10:36
# File: 0661.py
# Desc: 

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = 0, 0
        m = len(img)
        n = len(img[0])
        def parse(a,b):
            s = 0
            ct = 0
            for i in img[max(0,a-1):a+2]:
                for j in i[max(0,b-1):b+2]:
                    s += j
                    ct += 1
            return s//ct
        ret = []
        for i in range(m):
            ret.append([])
            for j in range(n):
                ret[-1].append(parse(i,j))
        return ret
