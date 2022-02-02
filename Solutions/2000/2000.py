# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/2 9:18
# File: 2000.py
# Desc: 

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word
        return word[word.find(ch):0:-1]+word[0]+word[word.find(ch)+1:]
