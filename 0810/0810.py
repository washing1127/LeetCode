# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/22 23:12
# File: 0810.py
# Desc: 

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        
        xorsum = reduce(xor, nums)
        return xorsum == 0

