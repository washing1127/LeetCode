# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/27 17:07
# File: 面试题 17.11.py
# Desc: 

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        l = None
        r = None
        ret = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                l = i
                if r: ret = min(ret, l-r)
            if words[i] == word2:
                r = i
                if l: ret = min(ret, r-l)
        return ret
