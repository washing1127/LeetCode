# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/12 10:28
# File: 1252.py
# Desc: 


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        sc = set()
        sr = set()
        for c, r in indices:
            if c in sc: sc.remove(c)
            else: sc.add(c)
            if r in sr: sr.remove(r)
            else: sr.add(r)
        return len(sc) * n - len(sc) * len(sr) + (m - len(sc)) * len(sr)
