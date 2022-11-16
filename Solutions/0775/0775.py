# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/16 10:24
# File: 0775.py
# Desc: 

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        mi = 0
        if 0 in nums[:2]:
            mi += 1
            if 1 in nums[:2]:
                mi += 1
        for idx,i in enumerate(nums):
            # print(idx,i,mi)
            if i > mi: return False
            while mi in nums[idx:idx+3]: mi+=1
        return True
