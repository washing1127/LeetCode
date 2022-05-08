# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/8 15:42
# File: 0442.py
# Desc: 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        s = set()
        for i in nums:
            if not i in s: s.add(i)
            else: ret.append(i)
        return ret
