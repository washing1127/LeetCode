# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/31 11:30
# File: 1374.py
# Desc: 



class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2: return 'a'*n
        else: return 'a'*(n-1)+'b'
