# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/20 06:21
# File: 2347.py
# Desc: 


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        c = collections.Counter(ranks)
        s = set(suits)
        if len(s) == 1: return "Flush"
        if max(c.values()) >= 3: return "Three of a Kind"
        if max(c.values()) == 2: return "Pair"
        return "High Card"
