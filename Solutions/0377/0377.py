# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/24 15:47
# File: 0377.py
# Desc: 

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]
