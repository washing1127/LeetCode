# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/1 20:21
# File: 2351.py
# Desc: 


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        se = set()
        for i in s:
            if i in se: return i
            se.add(i)
