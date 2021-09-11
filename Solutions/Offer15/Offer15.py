# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/23 10:26
# File: Offer15.py
# Desc: 

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
