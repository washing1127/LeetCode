# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/24 10:49
# File: 0664.py
# Desc: 

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        f = []
        for i in range(n):
            f.append([0]*n)
        for i in range(n-1,-1,-1):
            f[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i][j-1]
                else:
                    m = n
                    for k in range(i, j):
                        m = min(m, f[i][k] + f[k+1][j])
                    f[i][j] = m
        return f[0][n - 1]