# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/29 17:53
# File: 0517.py
# Desc: 

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        tot = sum(machines)
        n = len(machines)
        if tot % n:
            return -1
        avg = tot // n
        ans, s = 0, 0
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans

