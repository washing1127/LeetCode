# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/01/26 10:42
# File: 1663.py
# Desc: 


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = []
        for i in range(1, n + 1):
            lower = max(1, k - (n - i) * 26)
            k -= lower
            s.append(ascii_lowercase[lower - 1])
        return ''.join(s)
