# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/18 15:33
# File: 0136.py
# Desc: 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return functools.reduce(int.__xor__,nums)