# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/28 10:12
# File: 0693.py
# Desc: 

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return False if '00' in bin(n) or '11' in bin(n) else True
