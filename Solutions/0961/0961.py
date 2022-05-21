# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/21 11:54
# File: 0961.py
# Desc: 

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s: return i
            s.add(i)
