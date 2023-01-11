# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/11 10:21
# File: 2283.py
# Desc: 


class Solution:
    def digitCount(self, num: str) -> bool:
        c = collections.Counter(num)
        for idx, i in enumerate(num):
            if c[str(idx)] != int(i):
                return False
        return True
