# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/19 15:10
# File: 0345.py
# Desc: 

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = []
        S = set("aeiouAEIOU")
        for i in s:
            if i in S:
                l.append(i)
        li = list(s)
        for i in range(len(li)):
            if li[i] in S:
                li[i] = l.pop()

        return ''.join(li)