# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/2/23 10:42
# File: 0917.py
# Desc: 

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        li = list(s)
        l = 0; r = len(s)-1
        while l < r:
            while l<r and not li[l].isalpha(): l+=1
            while l<r and not li[r].isalpha(): r-=1
            li[l], li[r] = li[r], li[l]
            l+=1; r-=1
        return ''.join(li)
