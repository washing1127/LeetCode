# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/3/24 16:06
# File: 0456.py
# Desc: 

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = nums[0]
        for i in range(1, len(nums)-1):
            k = nums[i]
            if l >= k: 
                l = k
                continue
            for j in nums[i+1:]:
                if l < j < k:
                    return True
        return False