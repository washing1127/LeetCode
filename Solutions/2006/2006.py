# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/9 9:50
# File: 2006.py
# Desc: 

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j]) == k: ret += 1
        return ret
