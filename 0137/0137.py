# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/30 16:04
# File: 0137.py
# Desc: 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        for k, v in c.items():
            if v == 1: return k