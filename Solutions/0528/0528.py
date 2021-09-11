# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/30 11:01
# File: 0528.py
# Desc: 

class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)