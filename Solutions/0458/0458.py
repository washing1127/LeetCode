# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/11/25 14:53
# File: 0458.py
# Desc: 

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1
        return ceil(log(buckets) / log(states))

