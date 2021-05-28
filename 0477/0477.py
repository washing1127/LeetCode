# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/5/28 10:16
# File: 0477.py
# Desc: 

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans
