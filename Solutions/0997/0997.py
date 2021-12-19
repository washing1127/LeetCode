# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/19 17:11
# File: 0997.py
# Desc: 

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegrees = Counter(y for _, y in trust)
        outDegrees = Counter(x for x, _ in trust)
        return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)

