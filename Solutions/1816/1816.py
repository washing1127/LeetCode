# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/6 10:50
# File: 1816.py
# Desc: 

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split(' ',k)[:k])
