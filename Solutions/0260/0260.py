# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/30 22:42
# File: 0260.py
# Desc: 

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        return [i for i in c if c[i] == 1]

