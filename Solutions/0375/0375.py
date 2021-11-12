# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/12 15:47
# File: 0375.py
# Desc: 

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                f[i][j] = min(k + max(f[i][k - 1], f[k + 1][j]) for k in range(i, j))
        return f[1][n]

