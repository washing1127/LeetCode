# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/12/10 13:49
# File: 0748.py
# Desc: 

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        s=''.join([i.lower() for i in licensePlate if i.isalpha()])
        ret = 'a'*15
        c = collections.Counter(s)
        for word in words:
            flag = True
            for k,v in c.items():
                if word.count(k) < v: flag = False
            if flag and len(word) < len(ret): ret = word
        return ret

