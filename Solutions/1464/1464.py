# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/26 08:23
# File: 1464.py
# Desc: 


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # a=0
        # b=0
        # for i in nums:
        #     if i >= a:
        #         if i >= b:
        #             a = b
        #             b = i
        #         else:
        #             a = i
        # return (a-1)*(b-1)
        nums.sort()
        return (nums[-1]-1) * (nums[-2]-1)
