# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/12 10:21
# File: 2287.py
# Desc: 


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        n = len(s)
        c1 = collections.Counter(s)
        c2 = collections.Counter(target)
        for k,v in c2.items():
            n = min(n, c1[k]//v)
        return n
