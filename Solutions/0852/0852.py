# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/15 10:28
# File: 0852.py
# Desc: 

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
