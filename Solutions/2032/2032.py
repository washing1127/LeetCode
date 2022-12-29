# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/29 15:16
# File: 2032.py
# Desc: 


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s = set(nums1)
        ret = set()
        for i in set(nums2):
            if i in s: ret.add(i)
            else: s.add(i)
        for i in set(nums3):
            if i in s: ret.add(i)
            else: s.add(i)
        return  list(ret)
