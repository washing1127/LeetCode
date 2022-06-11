# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/11 18:11
# File: 0926.py
# Desc: CV


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0New, dp1New = dp0, min(dp0, dp1)
            if c == '1':
                dp0New += 1
            else:
                dp1New += 1
            dp0, dp1 = dp0New, dp1New
        return min(dp0, dp1)

