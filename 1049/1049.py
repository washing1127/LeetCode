# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/8 10:11
# File: 1049.py
# Desc: 

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums=sum(stones)
        dp=[0]*(sums//2+1)
        for x in stones:
            for i in range(sums//2,x-1,-1):
                dp[i]=max(dp[i],dp[i-x]+x)
        return sums-2*dp[sums//2]

