# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/19 18:56
# File: 0462.py
# Desc: 

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        return sum(abs(num - nums[len(nums) // 2]) for num in nums)

