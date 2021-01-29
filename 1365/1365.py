# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/29 18:43
# File: 1365.py
# Desc: 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
        nums2.sort()
        for idx, item in enumerate(nums):
            nums[idx] = nums2.index(item)
        return nums