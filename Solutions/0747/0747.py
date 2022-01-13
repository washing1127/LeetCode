# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/13 10:49
# File: 0747.py
# Desc: 

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        n = sorted(nums)
        if n[-2] == 0: return nums.index(n[-1])
        elif n[-1] // n[-2] >= 2:
            return nums.index(n[-1])
        return -1
