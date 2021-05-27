# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2020/5/27 9:55
# File: 0461.py
# Desc: 

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count("1")