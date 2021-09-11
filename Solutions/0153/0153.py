# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/8 13:52
# File: 0153.py
# Desc: 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]: return nums[0]
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]: return nums[i]