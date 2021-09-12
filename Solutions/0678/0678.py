# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/12 23:30
# File: 0678.py
# Desc: 

class Solution:
    def checkValidString(self, s: str) -> bool:
        l = []
        x = []
        for idx,i in enumerate(s):
            if i == "(": l.append(idx)
            if i == "*": x.append(idx)
            if i == ")":
                if l: l.pop()
                elif x: x.pop()
                else: return False
        for i in l[::-1]:
            if not x or x.pop() < i: return False
        return True
