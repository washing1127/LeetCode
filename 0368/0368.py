# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/23 11:34
# File: 0368.py
# Desc: 


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1: return nums
        l = len(nums)
        nums.sort()

        dp = [[i] for i in nums]
        
        for i in range(1, l):
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] == 0:
                    dp[i] = max(dp[j] + [nums[i]], dp[i],key=len)

        return max(dp,key=len)