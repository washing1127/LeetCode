# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/1 17:38
# File: 0165.py
# Desc: 
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n=max(version1.count("."), version2.count("."))
        l1 = [0] * (n+1)
        l2 = [0] * (n+1)
        for idx, num in enumerate(version1.split(".")):
            l1[idx] = int(num)
        for idx, num in enumerate(version2.split(".")):
            l2[idx] = int(num)
        for a, b in zip(l1, l2):
            if a > b: return 1
            elif a < b: return -1
        return 0