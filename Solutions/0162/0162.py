# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/15 17:38
# File: 0162.py
# Desc: 
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))
