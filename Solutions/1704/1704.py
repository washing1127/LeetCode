# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/11 11:35
# File: 1704.py
# Desc: 


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower().replace('a','u').replace('e','u').replace('i','u').replace('o','u')
        return s[:len(s)//2].count('u') * 2 == s.count('u')
