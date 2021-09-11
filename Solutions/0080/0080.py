# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/6 10:04
# File: 0080.py
# Desc: 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,-1,-1):
            if i - nums.index(nums[i]) >= 2:
                nums.pop(i)
        return len(nums)