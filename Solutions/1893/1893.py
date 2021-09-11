# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/23 22:29
# File: 1893.py
# Desc: 

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        l = []
        for i in ranges:
            l += list(range(i[0],i[1]+1))
        for i in range(left, right+1):
            if not i in l: return False
        return True
