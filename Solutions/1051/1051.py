# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/13 10:22
# File: 1051.py
# Desc: 

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if j != i else 0 for i,j in zip(heights, sorted(heights))])
