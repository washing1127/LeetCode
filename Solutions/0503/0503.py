# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/6 22:35
# File: 0503.py
# Desc: 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1]*n
        stk = []

        for i in range(n*2-1):
            idx = i % n
            while stk and nums[stk[-1]] < nums[idx]:
                ret[stk.pop()] = nums[idx]
            stk.append(idx)

        return ret