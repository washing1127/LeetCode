# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/01/28 10:42
# File: 1664.py
# Desc: 

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        l = []
        for idx,i in enumerate(nums):
            if idx == 0: last = [0,0]
            else: last = l[-1].copy()
            if idx % 2:
                last[1] += i
            else:
                last[0] += i
            l.append(last)
        # print(l)
        total_a, total_b = l[-1]
        # print(total_a, total_b)
        ret = 0
        for idx,(a,b) in enumerate(l):
            if idx % 2:
                last_a, last_b = a, b - nums[idx]
            else:
                last_a, last_b = a - nums[idx], b
            rest_a = total_b - b
            rest_b = total_a - a
            if last_a + rest_a == last_b + rest_b:
                ret += 1
            # print(nums[idx], last_a, rest_a, last_b, rest_b)
        return ret
