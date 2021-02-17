# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/17 20:37
# File: 0566.py
# Desc: 

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if nums and len(nums)*len(nums[0]) != r*c:
            return nums
        ret = []
        li = []
        a = 0
        for i in nums:
            for j in i:
                li.append(j)
                a += 1
                if a == c:
                    ret.append(li.copy())
                    li = []
                    a = 0
        return ret