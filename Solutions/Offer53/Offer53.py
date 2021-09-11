# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/16 11:26
# File: Offer53.py
# Desc: 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums, target, lower):
            l = 0
            r = len(nums) - 1
            ans = len(nums)
            while l <= r:
                m = (l+r)//2
                if nums[m] > target or (lower and nums[m] >= target):
                    r = m - 1
                    ans = m
                else:
                    l = m + 1
            return ans

        l = bs(nums, target, True)
        r = bs(nums, target, False) - 1
        if l <= r and r < len(nums) and nums[l] == nums[r] == target:
            return r - l + 1
        return 0
