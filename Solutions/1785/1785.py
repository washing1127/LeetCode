# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/16 11:17
# File: 1785.py
# Desc: 

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        sm = sum(nums)
        left = abs(goal - sm)
        ret = left // limit
        if left % limit: ret += 1
        return ret
