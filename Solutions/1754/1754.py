# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/24 17:03
# File: 1754.py
# Desc: 


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        i, j, n, m = 0, 0, len(word1), len(word2)
        while i < n or j < m:
            if i < n and word1[i:] > word2[j:]:
                merge.append(word1[i])
                i += 1
            else:
                merge.append(word2[j])
                j += 1
        return ''.join(merge)

