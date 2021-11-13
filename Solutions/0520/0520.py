# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/13 11:33
# File: 0520.py
# Desc: 

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
