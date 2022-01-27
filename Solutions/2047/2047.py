# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/27 10:28
# File: 2047.py
# Desc: 

class Solution:
    def countValidWords(self, sentence: str) -> int:
        ret = 0
        for i in sentence.split(" "):
            if not i: continue
            if len(i) == 1 and i not in "-0123456789": 
                ret += 1
                print(i)
                continue
            if i[-1] in '.,!': i=i[:-1]
            if i.isalpha() or i.count("-")==1 and i.split("-")[0].isalpha() and i.split("-")[1].isalpha():
                print(i)
                ret += 1
        return ret
