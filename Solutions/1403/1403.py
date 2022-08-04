# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/4 11:30
# File: 1403.py
# Desc: 


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        nums.sort(reverse=True)
        ret = []
        s2 = 0
        for i in nums:
            s -= i
            s2 += i
            ret.append(i)
            if s2 > s: return ret
