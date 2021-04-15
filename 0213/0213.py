# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/15 10:42
# File: 0213.py
# Desc: 

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        dp1 = [0, nums[0]]
        dp2 = [0, 0]
        for i in range(1, len(nums)):
            dp1[:] = max(dp1[0], dp1[1]), dp1[0] + nums[i]
            dp2[:] = max(dp2[0], dp2[1]), dp2[0] + nums[i]
        return max(dp1[0], dp2[0], dp2[1]) 