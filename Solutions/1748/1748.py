# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/6 9:39
# File: 1748.py
# Desc: 

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k,v in collections.Counter(nums).items() if v == 1)
