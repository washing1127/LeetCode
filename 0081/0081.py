# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/7 13:45
# File: 0081.py
# Desc: 

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ma = nums.index(max(nums))
        mi = nums.index(min(nums))
        if nums[0] <= target:
            nums = nums[:ma+1]
        else:
            nums = nums[mi:]
        a = 0
        b = len(nums)
        while a < b:
            c = (a + b) // 2
            if nums[c] == target: return True
            elif nums[c] > target:
                b = c
            else:
                a = c + 1
        return False