# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/29 17:10
# File: 0035
# Desc: 

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if not nums: return 0
        for i in range(len(nums)):
            if nums[i] >= target: return i
        return i + 1
