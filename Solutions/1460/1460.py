# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/24 14:23
# File: 1460.py
# Desc: 


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)
