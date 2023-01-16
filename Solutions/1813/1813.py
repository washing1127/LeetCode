# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/16 10:50
# File: 1813.py
# Desc: 



class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1 = sentence1.split(' ')
        l2 = sentence2.split(' ')
        while l1 and l2 and l1[0] == l2[0]:
            l1.pop(0)
            l2.pop(0)
        while l1 and l2 and l1[-1] == l2[-1]:
            l1.pop()
            l2.pop()
        return len(l2) == 0 or len(l1) == 0
