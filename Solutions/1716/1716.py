# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/15 10:42
# File: 1716.py
# Desc: 
class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = 1, 1
        res = 0
        for i in range(n):
            res += week + day - 1
            day += 1
            if day == 8:
                day = 1
                week += 1
        return res



