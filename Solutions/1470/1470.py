# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/29 10:10
# File: 1470.py
# Desc: 

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = list()
        for i in range(n):
            ret.append(nums[i])
            ret.append(nums[i+n])
        return ret
