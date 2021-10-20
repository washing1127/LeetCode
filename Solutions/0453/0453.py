# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/20 16:06
# File: 0453.py
# Desc: 

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        ret = 0
        for i in nums:
            ret += i - m
        return ret
