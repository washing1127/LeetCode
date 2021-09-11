# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/4 00:28
# File: 0645.py
# Desc: 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ret = [0, 0]
        c = collections.Counter(nums)
        for i in range(1,len(nums)+1):
            if c[i] == 0:
                ret[1] = i 
            if c[i] == 2:
                ret[0] = i

        return ret
