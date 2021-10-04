# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/4 15:35
# File: 0482.py
# Desc: 
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        l = []
        ct = 0
        subs = ''
        for i in s[::-1]:
            if i == '-': continue
            ct += 1
            subs = i + subs
            if ct == k:
                ct = 0
                l.insert(0, subs)
                subs = ''
        if subs:
            l.insert(0, subs)
        return '-'.join(l).upper()
