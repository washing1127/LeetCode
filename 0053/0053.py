# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/10 17:06
# File: 0053.py
# Desc: 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sumNum = 0
        for i in nums:
            if sumNum > 0:
                sumNum += i
            else:
                sumNum = i
            res = max(res, sumNum)

        return res