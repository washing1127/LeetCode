# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/27 17:03
# File: 1752.py
# Desc: 


class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        n2 = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: break
        else: return True
        nums = nums[i+1:]+nums[:i+1]
        return nums == n2
