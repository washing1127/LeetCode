# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/20 10:34
# File: 1877.py
# Desc: 
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        ret = 0
        while l < r:
            ret = max(ret, nums[l]+nums[r])
            l += 1
            r -= 1
        return ret
