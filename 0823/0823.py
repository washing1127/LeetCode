# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/24 11:23
# File: 0823.py
# Desc: 

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
            for j in range(len(i)):
                i[j] = 0 if i[j] else 1
        return A