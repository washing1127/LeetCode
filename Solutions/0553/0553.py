# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/27 12:00
# File: 0553.py
# Desc: 

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return nums[0] + "/" + nums[1]
        nums[1] = "(" + nums[1]
        nums[-1] += ")"
        s = "/".join(nums)
        return s
