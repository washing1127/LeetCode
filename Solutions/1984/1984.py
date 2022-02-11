# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/11 10:41
# File: 1984.py
# Desc: 

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = nums[-1]
        for i in range(len(nums)-k+1):
            j=i+k-1
            ret = min(nums[j]-nums[i], ret)
        return ret
