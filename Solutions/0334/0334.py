# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/12 10:30
# File: 0334.py
# Desc: 


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        zx = nums[0]
        ex = None
        for i in nums[1:]:
            if i < zx: zx = i
            elif i > zx:
                if ex is None: ex = i
                else:
                    if i > ex:  return True
                    else: ex = i
        return False
