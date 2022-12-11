# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/11 10:35
# File: 1827.py
# Desc: 


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ret = 0
        for i in range(1,len(nums)):
            ret += max(nums[i-1]+1-nums[i], 0)
            nums[i] = max(nums[i], nums[i-1]+1)
        return ret
