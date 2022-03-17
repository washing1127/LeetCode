# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/17 16:39
# File: 0720.py
# Desc: 

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ret = ""
        s = set()
        for i in words:
            if len(i) == 1 or i[:-1] in s:
                s.add(i)
                if len(i) > len(ret): ret = i
        return ret
