# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/14 11:51
# File: 0540.py
# Desc: 

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        if r == 1: return nums[0]
        while l < r-1:
            m = (l+r) // 2
            if m % 2: # m是奇数
                if nums[m] == nums[m-1]: # 前面都是成对出现的
                    l = m+1
                else: # 前面有单独出现的
                    r = m
            else: # m是偶数
                if m == 0: return nums[m]
                if nums[m] == nums[m-1]: # 前面有单独出现的
                    r = m
                else: # 前面都是成对出现的
                    l = m
        return nums[l]
