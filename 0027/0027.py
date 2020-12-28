# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/12/28 17:47
# File: 0027
# Desc: 

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        i = 0
        num = 0
        while i < len(nums):
            if not val == nums[i]:
                num += 1
                i += 1
            else:
                nums.remove(nums[i])
        return num
