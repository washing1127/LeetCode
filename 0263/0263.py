# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/10 18:42
# File: 0263.py
# Desc: 

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        elif n <= 3: return True
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True