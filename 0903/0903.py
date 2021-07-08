# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/8 11:16
# File: 0903.py
# Desc: 
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        l1 = l2 = r = s1 = s2 = ret = 0
        while r < n:
            s1 += nums[r]
            while l1 <= r and s1 > goal:
                s1 -= nums[l1]
                l1 += 1
            s2 += nums[r]
            while l2 <= r and s2 >= goal:
                s2 -= nums[l2]
                l2 += 1
            ret += l2 - l1
            r += 1
        return ret

