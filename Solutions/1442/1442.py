# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/18 12:58
# File: 1442.py
# Desc: 
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        s = [0]
        for val in arr:
            s.append(s[-1] ^ val)
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if s[i] == s[k + 1]:
                        ans += 1
        
        return ans
