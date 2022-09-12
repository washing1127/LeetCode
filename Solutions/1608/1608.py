# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/12 10:40
# File: 1608.py
# Desc: 


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1

