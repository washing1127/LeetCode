# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/3 18:11
# File: 0829.py
# Desc: CV


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def isKConsecutive(n: int, k: int) -> bool:
            if k % 2:
                return n % k == 0
            return n % k and 2 * n % k == 0

        ans = 0
        k = 1
        while k * (k + 1) <= n * 2:
            if isKConsecutive(n, k):
                ans += 1
            k += 1
        return ans

