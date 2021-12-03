# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/3 14:13
# File: 1005.py
# Desc: 

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] >= 0:
            if k % 2:
                nums[0] = -nums[0]
            return sum(nums)
        fs = 0
        for i in range(k):
            if i<len(nums) and nums[i] < 0: nums[i] = -nums[i]
            else: break
        else:
            return sum(nums)
        if i == len(nums):
            if (k-i)%2:
                nums[-1] = -nums[-1]
            return sum(nums)
        a = nums[i-1]
        b = nums[i]
        if a < b:
            if (k-i)%2: nums[i-1] = -a
        elif (k-i)%2: nums[i] = -b 
        return sum(nums)
