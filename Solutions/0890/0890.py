# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/12 17:05
# File: 0890.py
# Desc: 

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def parse(pat):
            l = []
            s = ''
            for i in pat:
                if not i in l: l.append(i)
                s += str(l.index(i))
            return s
        p = parse(pattern)
        ret = []
        for i in words:
            if parse(i) == p: ret.append(i)
        return ret
