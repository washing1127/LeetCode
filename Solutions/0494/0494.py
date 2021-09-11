# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/6/7 11:44
# File: 0494.py
# Desc: 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        diff = s - target
        if diff < 0 or diff % 2 != 0: return 0
        neg = diff // 2
        dp = [0] * (neg+1)
        dp[0] = 1
        for num in nums:
            for j in range(neg, num-1, -1):
                dp[j] += dp[j-num]
        return dp[neg]

