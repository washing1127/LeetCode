# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/9 9:30
# File: 1413.py
# Desc: 

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return max(1, -min(nums)+1)
