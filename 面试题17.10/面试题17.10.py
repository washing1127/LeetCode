# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/9 14:07
# File: 面试题 17.10.py
# Desc: 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        mn = nums[length//2]
        if nums.count(mn) > length / 2: return mn
        return -1