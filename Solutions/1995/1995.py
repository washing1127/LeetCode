# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/29 10:21
# File: 1995.py
# Desc: 

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    ret += nums[k+1:].count(nums[i] + nums[j] + nums[k])
        return ret
