# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/5 12:07
# File: 1208.py
# Desc: 
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # totalCost = 0
        # li = []
        # count = 0
        # for c1, c2 in zip(s, t):
        #     num = abs(ord(c1) - ord(c2))
        #     totalCost += num
        #     li.insert(0, num)
        #     while totalCost > maxCost:
        #         totalCost -= li.pop()
        #     count = max(count, len(li))
        # return count
        l = r = 0
        totalCost = 0
        for c1, c2 in zip(s, t):
            r += 1
            num = abs(ord(c1) - ord(c2))
            totalCost += num
            if totalCost > maxCost:
                totalCost -= abs(ord(s[l])-ord(t[l]))
                l += 1
        return r - l