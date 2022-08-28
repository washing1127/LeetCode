# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/28 8:48
# File: 0793.py
# Desc: CV


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(n: int) -> int:
            res = 0
            while n:
                n //= 5
                res += n
            return res

        def nx(k: int) -> int:
            return bisect_left(range(5 * k), k, key=zeta)

        return nx(k + 1) - nx(k)

