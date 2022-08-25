# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/25 09:49
# File: 0658.py
# Desc: 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = [[i, abs(i-x)] for i in arr]
        l.sort(key=lambda x: (x[1], x[0]))
        return sorted([i[0] for i in l[:k]])
