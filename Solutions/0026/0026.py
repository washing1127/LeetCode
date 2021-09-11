# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/18 17:39
# File: 0026.py
# Desc: 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)