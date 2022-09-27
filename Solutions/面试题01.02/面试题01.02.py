# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/13 10:50
# File: ÃæÊÔÌâ01.02.py
# Desc: 

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)
