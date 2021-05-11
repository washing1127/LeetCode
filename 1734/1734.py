# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/11 10:39
# File: 1734.py
# Desc: 
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n+1):
            total ^= i
        odd = 0
        for i in range(1, n - 1, 2):
            odd ^= encoded[i]
        
        perm = [total ^ odd]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])

        return perm
