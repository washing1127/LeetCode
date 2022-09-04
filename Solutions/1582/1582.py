# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/4 16:28
# File: 1582.py
# Desc: 


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        l = 0
        for idx, i in enumerate(mat):
            if sum(i) != 1: continue
            for jdx, num in enumerate(i):
                if num == 1 and sum([i[jdx] for i in mat]) == 1:
                    l += 1
        return l
