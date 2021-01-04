# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/1/4 12:55
# File: 0509.py
# Desc: 

class Solution:
    def fib(self, n: int) -> int:
        return self.fib(n-1) + self.fib(n-2) if n > 1 else n