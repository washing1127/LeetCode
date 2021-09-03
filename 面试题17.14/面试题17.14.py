# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/3 14:07
# File: 面试题 17.14.py
# Desc: 

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]