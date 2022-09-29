# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/13 10:50
# File: 面试题 01.09.py
# Desc: 


class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s1 in s2*2
