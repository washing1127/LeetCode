# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/7 10:37
# File: 1486.py
# Desc: 

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2*i)
        ret = nums[0]
        for i in nums[1:]:
            ret ^= i 
        return ret
