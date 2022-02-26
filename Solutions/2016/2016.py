# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/26 11:01
# File: 2016.py
# Desc: 

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        a = nums[0]
        ma = -1
        for i in nums[1:]:
            if i > a: ma = max(i-a, ma)
            else: a = i
        return ma
