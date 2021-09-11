# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/26 18:44
# File: 0169.py
# Desc: 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if not c:
                a = i
                c += 1
            elif i == a:
                c += 1
            else:
                c -= 1
        return a