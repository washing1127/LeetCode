# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/21 21:53
# File: 1438.py
# Desc: 

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0

        max_i = min_i = nums[0]

        for idx, num in enumerate(nums):
            if max_i-min_i > limit or abs(min_i-num) > limit or abs(max_i-num) > limit:
                left += 1
                min_i = min(nums[left: idx+1])
                max_i = max(nums[left: idx+1])
            elif num < min_i: min_i = num
            elif num > max_i: max_i = num
        return idx-left+1
