# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/22 10:07
# File: 0878.py
# Desc: 


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        c = lcm(a, b)
        m = c // a + c // b - 1
        r = n % m
        res = c * (n // m) % MOD
        if r == 0:
            return res
        addA = a
        addB = b
        for _ in range(r - 1):
            if addA < addB:
                addA += a
            else:
                addB += b
        return (res + min(addA, addB) % MOD) % MOD
