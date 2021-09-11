# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/23 22:33
# File: 0191.py
# Desc: 
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')