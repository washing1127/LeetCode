# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/23 10:03
# File: 1768.py
# Desc: 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = list()
        n = min(len(word1), len(word2))
        for i in range(n):
            s.append(word1[i])
            s.append(word2[i])
        return ''.join(s) + word1[n:] + word2[n:]
