# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/2/15 17:02
# File: 0485.py
# Desc: 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        for idx in range(1, len(nums)):
            if nums[idx]:
                nums[idx] += nums[idx-1]
        return max(nums)