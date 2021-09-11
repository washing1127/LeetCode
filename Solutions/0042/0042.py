# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/3 11:23
# File: 0042.py
# Desc: 

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        total = 0
        left_num = 0
        left_idx = 0
        right_num = 0
        right_idx = length
        for idx in range(length):
            num = height[idx]
            right = length-idx-1
            num2 = height[right]
            if num >= left_num:
                total += left_num * (idx-left_idx-1) - sum(height[left_idx+1:idx])
                left_num = num
                left_idx = idx
            if num2 > right_num:
                total += right_num * (right_idx-right-1) - sum(height[right+1:right_idx])
                right_num = num2
                right_idx = right
        return total