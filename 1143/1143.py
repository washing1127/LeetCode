# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/3 18:12
# File: 1143.py
# Desc: 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        l = [0] * (n+1)
        temp = []
        for i in range(m+1):
            temp.append(l.copy())
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    temp[i+1][j+1] = temp[i][j] + 1
                else:
                    temp[i+1][j+1] = max(temp[i][j+1], temp[i+1][j])

        return temp[-1][-1]
