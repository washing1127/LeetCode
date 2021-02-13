# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/2/13 16:59
# File: 0448.py
# Desc: 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        c = collections.Counter(range(1, len(nums)+1))
        for i in set(nums):
            c[i] -= 1
        ret = []
        for i in c:
            if c[i]:
                ret.append(i)
        return ret
