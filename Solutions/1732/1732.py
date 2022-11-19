# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/18 15:12
# File: 1732.py
# Desc: 

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(1,len(gain)):gain[i] += gain[i-1]
        return max(max(gain), 0)
