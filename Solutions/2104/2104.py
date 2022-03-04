# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/3/3 20:21
# File: 2104.py
# Desc: CV

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            minVal, maxVal = inf, -inf
            for j in range(i, n):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                ans += maxVal - minVal
        return ans

