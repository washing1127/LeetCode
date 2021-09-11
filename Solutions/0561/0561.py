# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/16 11:35
# File: 0561.py
# Desc: 
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])