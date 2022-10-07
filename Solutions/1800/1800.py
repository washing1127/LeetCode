# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/7 10:50
# File: 1800.py
# Desc: 

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = ret = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                temp = nums[i]
            ret = max(temp, ret)
        return ret
