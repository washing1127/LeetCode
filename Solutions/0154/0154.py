# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/9 10:17
# File: 0154.py
# Desc: 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[r] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m + 1
            else:
                r -= 1
        return nums[l]