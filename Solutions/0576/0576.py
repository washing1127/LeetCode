# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/15 16:24
# File: 0576.py
# Desc: 

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        outCounts = 0
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        for i in range(maxMove):
            dpNew = [[0] * n for _ in range(m)]
            for j in range(m):
                for k in range(n):
                    if dp[j][k] > 0:
                        for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                            if 0 <= j1 < m and 0 <= k1 < n:
                                dpNew[j1][k1] = (dpNew[j1][k1] + dp[j][k]) % MOD
                            else:
                                outCounts = (outCounts + dp[j][k]) % MOD
            dp = dpNew
        
        return outCounts
