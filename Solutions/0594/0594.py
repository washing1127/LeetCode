# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/20 10:40
# File: 0594.py
# Desc: 

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        ret = 0
        for num in nums:
            if num+1 in c.keys():
                ret = max(ret, c[num] + c[num+1])
        return ret
