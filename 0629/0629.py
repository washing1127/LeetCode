# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/20 10:53
# File: 0629.py
# Desc: 
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = collections.Counter(words)
        keys = list(c.keys())
        keys.sort(reverse=True)
        keys.sort(key=lambda i: c[i])
        li = []
        for i in range(k):
            key = keys[-1-i]
            v = key
            li.append(v)

        return li