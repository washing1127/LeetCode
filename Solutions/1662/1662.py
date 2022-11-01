# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/01 10:42
# File: 1662.py
# Desc: 


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
