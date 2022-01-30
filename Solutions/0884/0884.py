# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/30 10:42
# File: 0884.py
# Desc: 

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = collections.Counter(s1.split(" "))
        c2 = collections.Counter(s2.split(" "))
        ret = []
        for k,v in c1.items():
            if v == 1 and k not in c2: ret.append(k)
        for k,v in c2.items():
            if v == 1 and k not in c1: ret.append(k)
        return ret
