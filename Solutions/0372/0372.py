# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/5 21:45
# File: 0372.py
# Desc: CV

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        ans = 1
        for e in b:
            ans = pow(ans, 10, MOD) * pow(a, e, MOD) % MOD
        return ans

