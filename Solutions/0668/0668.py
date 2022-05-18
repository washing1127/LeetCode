# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/18 10:28
# File: 0668.py
# Desc: CV

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        return bisect_left(range(m * n), k, key=lambda x: x // n * n + sum(x // i for i in range(x // n + 1, m + 1)))



