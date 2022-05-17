# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/5/17 11:00
# File: 0953.py
# Desc: 

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        s = 'abcdefghijklmnopqrstuvwxyz'
        for idx, w in enumerate(words):
            nw = ''
            for i in w:
                nw += s[order.find(i)]
            words[idx] = nw
        return sorted(words) == words
