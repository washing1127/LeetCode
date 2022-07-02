# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/2 09:57
# File: 0871.py
# Desc: CV

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        return next((i for i, v in enumerate(dp) if v >= target), -1)

