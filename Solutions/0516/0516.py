# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/12 10:51
# File: 0516.py
# Desc: 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = []
        for i in range(n):
            subl = [0]*n
            subl[i] = 1
            dp.append(subl)
            
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]