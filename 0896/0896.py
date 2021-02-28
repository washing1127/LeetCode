# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/28 17:05
# File: 0896.py
# Desc: 

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A, reverse=True)