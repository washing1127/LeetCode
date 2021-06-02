# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/2 11:33
# File: 0523.py
# Desc: 

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            presum += num
            presum %= k
            if presum in modes:
                return True
            modes.add(last)
        return False

