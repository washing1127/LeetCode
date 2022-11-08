# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/8 10:10
# File: 1684.py
# Desc: 

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ret = 0
        s = set(allowed)
        for word in words:
            for j in set(word):
                if j not in s: break
            else: ret+=1
        return ret
