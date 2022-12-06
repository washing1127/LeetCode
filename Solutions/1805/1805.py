# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/6 10:50
# File: 1805.py
# Desc: 

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        p = re.compile('[a-zA-Z]')
        l = p.split(word)
        for i in l:
            if i and int(i) not in s:
                s.add(int(i))
        return len(s)
