# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/17 10:50
# File: 1814.py
# Desc: 


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n):
            return int(str(n)[::-1])
        d = dict()
        for idx, num1 in enumerate(nums):
            num2 = rev(num1)
            cha = num1 - num2
            if cha not in d: d[cha] = set()
            d[cha].add(idx)
        ret = 0
        for v in d.values():
            l = len(v) - 1
            ret += (l+1) * l // 2
        return ret % (10**9+7)
