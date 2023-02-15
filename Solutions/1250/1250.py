# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/15 10:28
# File: 1250.py
# Desc: CV


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(gcd, nums) == 1
