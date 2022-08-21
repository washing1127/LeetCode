# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/21 19:23
# File: 1455.py
# Desc: 


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, i in enumerate(sentence.split(" ")):
            if i.startswith(searchWord): return idx+1
        return -1
