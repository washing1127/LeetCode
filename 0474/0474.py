# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/6/6 18:56
# File: 0474.py
# Desc: 
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def num_counter(strs):
            num01 = []
            num01.append(strs.count("0"))
            num01.append(strs.count("1"))
            return num01

        dp = []
        for i in range(m+1):
            dp.append([0]*(n+1))
        length = len(strs)
        for i in range(length):
            num01 = num_counter(strs[i])
            num0 = num01[0]
            num1 = num01[1]
            for j in range(m, num0-1, -1):
                for k in range(n, num1-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-num0][k-num1]+1)
        return dp[m][n]
