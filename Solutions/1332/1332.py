# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/22 23:21
# File: 1332.py
# Desc: 

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2

