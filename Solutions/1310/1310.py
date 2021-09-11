# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/12 10:06
# File: 1310.py
# Desc: 
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        acc = list(accumulate([0] + arr, xor))
        return [acc[a] ^ acc[b + 1] for a, b in queries]