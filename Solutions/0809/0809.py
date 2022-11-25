# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/25 23:12
# File: 0809.py
# Desc: 


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        l1 = []
        for i in s:
            if not l1 or l1[-1][0] != i:
                l1.append(i)
            else:
                l1[-1] += i
        ret = 0
        for word in words:
            l2 = []
            for i in word:
                if not l2 or l2[-1][0] != i:
                    l2.append(i)
                else:
                    l2[-1] += i
            if len(l1) != len(l2): continue
            for a,b in zip(l1,l2):
                # print(a,b)
                if len(a) != len(b) and len(a) < 3 or len(a) < len(b) or a[0] != b[0]:
                    break
            else: ret += 1
        return ret
