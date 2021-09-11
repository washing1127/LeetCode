# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/4 17:48
# File: 0643.py
# Desc: 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxnum = sum(nums[:k])
        num = maxnum
        for i in range(1,len(nums)-k+1):
            num = num-nums[i-1]+nums[i+k-1]
            maxnum = max(maxnum, num)
        return maxnum/k