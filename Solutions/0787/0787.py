# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/24 21:05
# File: 0787.py
# Desc: 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)
        
        ans = min(f[t][dst] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans
