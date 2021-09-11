# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/9 10:41
# File: 1047.py
# Desc: 

class Solution:

    def func(self, s, l, r):
        while l > 0 and r < len(s) - 1 and s[l-1] == s[r+1]:
            l -= 1
            r += 1
        return l, r

    def removeDuplicates(self, S: str) -> str:
        s = S
        s2 = ""
        while True:
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    l, r = self.func(s, i, i+1)
                    if l == 0:
                        s3 = s2[-1:]
                        s2 = s2[:-1]
                        s = s3 + s[r+1:]
                    else:
                        s2 += s[:l]
                        s = s[r+1:]
                    break
            else:
                return s2+s
