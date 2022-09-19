# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/19 10:02
# File: 1636.py
# Desc: 


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda x: (collections.Counter(nums)[x], -x))
