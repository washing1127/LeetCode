# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/3 13:28
# File: 0581.py
# Desc: 

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        f1 = f2 = True
        l = r = 0
        length = len(nums)
        for idx in range(length):
            l1 = nums[idx]
            l2 = nums2[idx]
            r1 = nums[length-idx-1]
            r2 = nums2[length-idx-1]
            if f1 is True and l1 != l2:
                l = idx
                f1 = False
            if f2 is True and r1 != r2:
                r = length-idx-1
                f2 = False
        if l == r == 0: return 0
        return r-l+1