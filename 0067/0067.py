# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/13 10:53
# File: 0067.py
# Desc: 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]