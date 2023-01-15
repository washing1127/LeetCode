# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/15 10:21
# File: 2293.py
# Desc: 


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        newNums = [0] * (n // 2)
        for i in range(n // 2):
            if i % 2 == 0:
                newNums[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                newNums[i] = max(nums[2 * i], nums[2 * i + 1])
        return self.minMaxGame(newNums)
